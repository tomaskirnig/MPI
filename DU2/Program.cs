using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;

class Program
{
    static void Main()
    {
        var tokens = Tokenize(Console.In).GetEnumerator();
        if (!tokens.MoveNext()) return;

        int T = int.Parse(tokens.Current);
        Random rng = new Random();

        for (int testCase = 1; testCase <= T; testCase++)
        {
            tokens.MoveNext();
            int N = int.Parse(tokens.Current);
            tokens.MoveNext();
            int D = int.Parse(tokens.Current);
            tokens.MoveNext();
            int m = int.Parse(tokens.Current);
            tokens.MoveNext();
            int R = int.Parse(tokens.Current);

            double[,] X = new double[N, D];
            for (int i = 0; i < N; i++)
            {
                for (int j = 0; j < D; j++)
                {
                    tokens.MoveNext();
                    X[i, j] = double.Parse(tokens.Current, CultureInfo.InvariantCulture);
                }
            }

            int[] dims = new int[m];
            for (int i = 0; i < m; i++)
            {
                tokens.MoveNext();
                dims[i] = int.Parse(tokens.Current);
            }

            tokens.MoveNext();
            double q = double.Parse(tokens.Current, CultureInfo.InvariantCulture);
            tokens.MoveNext();
            double epsMds = double.Parse(tokens.Current, CultureInfo.InvariantCulture);
            tokens.MoveNext();
            double epsRp = double.Parse(tokens.Current, CultureInfo.InvariantCulture);

            // Compute delta and sumDeltaSq
            double[,] delta = new double[N, N];
            double sumDeltaSq = 0.0;
            for (int i = 0; i < N; i++)
            {
                for (int j = i + 1; j < N; j++)
                {
                    double dist = Distance(X, i, j, D);
                    delta[i, j] = delta[j, i] = dist;
                    sumDeltaSq += dist * dist;
                }
            }

            // PCA: Center X
            double[,] Xc = new double[N, D];
            for (int j = 0; j < D; j++)
            {
                double mean = 0.0;
                for (int i = 0; i < N; i++) mean += X[i, j];
                mean /= N;
                for (int i = 0; i < N; i++) Xc[i, j] = X[i, j] - mean;
            }

            // G = Xc^T * Xc
            double[,] G = new double[D, D];
            for (int p = 0; p < D; p++)
            {
                for (int qCol = 0; qCol < D; qCol++)
                {
                    double sum = 0.0;
                    for (int i = 0; i < N; i++) sum += Xc[i, p] * Xc[i, qCol];
                    G[p, qCol] = sum;
                }
            }

            // Jacobi rotations
            double[,] H = (double[,])G.Clone();
            double[,] V = new double[D, D];
            for (int i = 0; i < D; i++) V[i, i] = 1.0;

            double maxGpp = 0.0;
            for (int i = 0; i < D; i++)
                if (G[i, i] > maxGpp) maxGpp = G[i, i];
            double eta = 1e-12 * maxGpp;

            for (int sweep = 0; sweep < 50; sweep++)
            {
                bool rotated = false;
                for (int p = 0; p < D - 1; p++)
                {
                    for (int qCol = p + 1; qCol < D; qCol++)
                    {
                        if (Math.Abs(H[p, qCol]) <= eta) continue;
                        rotated = true;

                        double a = H[p, p], b = H[p, qCol], e = H[qCol, qCol];
                        double tau = (e - a) / (2.0 * b);
                        double sgn = tau >= 0.0 ? 1.0 : -1.0;
                        double t = sgn / (Math.Abs(tau) + Math.Sqrt(1.0 + tau * tau));
                        double c = 1.0 / Math.Sqrt(1.0 + t * t);
                        double s = t * c;

                        for (int k = 0; k < D; k++)
                        {
                            if (k != p && k != qCol)
                            {
                                double u = H[k, p], v = H[k, qCol];
                                H[k, p] = H[p, k] = c * u - s * v;
                                H[k, qCol] = H[qCol, k] = s * u + c * v;
                            }
                        }
                        H[p, p] = a - t * b;
                        H[qCol, qCol] = e + t * b;
                        H[p, qCol] = H[qCol, p] = 0.0;

                        for (int k = 0; k < D; k++)
                        {
                            double u = V[k, p], v = V[k, qCol];
                            V[k, p] = c * u - s * v;
                            V[k, qCol] = s * u + c * v;
                        }
                    }
                }
                if (!rotated) break;
            }

            double[] lambdas = new double[D];
            for (int i = 0; i < D; i++) lambdas[i] = H[i, i] <= eta ? 0.0 : H[i, i];

            var order = Enumerable.Range(0, D)
                .OrderByDescending(i => lambdas[i])
                .ThenBy(i => i)
                .ToArray();

            double[] sortedLambdas = order.Select(i => lambdas[i]).ToArray();
            double[,] sortedV = new double[D, D];
            for (int r = 0; r < D; r++)
                for (int col = 0; col < D; col++)
                    sortedV[r, col] = V[r, order[col]];

            double totalLambda = sortedLambdas.Sum();

            Console.WriteLine($"Case {testCase}:");

            int minPca = -1, minMds = -1, minRp = -1;

            foreach (int d in dims)
            {
                // Y_pca = Xc * V_d
                double[,] Y_pca = new double[N, d];
                for (int i = 0; i < N; i++)
                {
                    for (int j = 0; j < d; j++)
                    {
                        if (sortedLambdas[j] == 0.0)
                        {
                            Y_pca[i, j] = 0.0;
                            continue;
                        }
                        double sum = 0.0;
                        for (int k = 0; k < D; k++)
                            sum += Xc[i, k] * sortedV[k, j];
                        Y_pca[i, j] = sum;
                    }
                }

                bool allPos = (d >= D) || (sortedLambdas[d] == 0.0) || (totalLambda == 0.0);
                double cevr = allPos ? 1.0 : (sortedLambdas.Take(d).Sum() / totalLambda);

                double[,] rhoPca = ComputeRho(Y_pca, N, d);
                double fPca = RawStress(rhoPca, delta, N);
                double sPca = Math.Sqrt(fPca / sumDeltaSq);
                double kPca = ConcentrationK(rhoPca, N);

                // Metric MDS (SMACOF)
                double[,] Y_mds = (double[,])Y_pca.Clone();
                double[,] rhoCurr = (double[,])rhoPca.Clone();
                double fPrev = fPca;

                for (int update = 1; update <= 500; update++)
                {
                    double[,] U = new double[N, d];
                    for (int i = 0; i < N; i++)
                    {
                        for (int j = i + 1; j < N; j++)
                        {
                            double dist = rhoCurr[i, j];
                            if (dist > 0.0)
                            {
                                double r = delta[i, j] / dist;
                                for (int k = 0; k < d; k++)
                                {
                                    double diff = r * (Y_mds[i, k] - Y_mds[j, k]);
                                    U[i, k] += diff;
                                    U[j, k] -= diff;
                                }
                            }
                        }
                    }

                    double[,] Y_next = new double[N, d];
                    for (int i = 0; i < N; i++)
                        for (int k = 0; k < d; k++)
                            Y_next[i, k] = U[i, k] / N;

                    double[,] rhoNext = ComputeRho(Y_next, N, d);
                    double Q = 0.0;
                    for (int i = 0; i < N; i++)
                        for (int j = i + 1; j < N; j++)
                            Q += rhoNext[i, j] * rhoNext[i, j];

                    if (Q == 0.0)
                    {
                        Y_mds = Y_next;
                        rhoCurr = rhoNext;
                        break;
                    }

                    double fNext = RawStress(rhoNext, delta, N);
                    if (update >= 2 && (fPrev - fNext) / Q < 1e-6)
                    {
                        Y_mds = Y_next;
                        rhoCurr = rhoNext;
                        break;
                    }

                    Y_mds = Y_next;
                    rhoCurr = rhoNext;
                    fPrev = fNext;
                }

                double fMds = RawStress(rhoCurr, delta, N);
                double sMds = Math.Sqrt(fMds / sumDeltaSq);
                double kMds = ConcentrationK(rhoCurr, N);

                // Random projection
                double sumS_Rp = 0.0;
                double sumK_Rp = 0.0;
                bool hasMinusOne = false;
                double scale = Math.Sqrt(3.0 / d);

                for (int rep = 0; rep < R; rep++)
                {
                    double[,] A = new double[D, d];
                    for (int p = 0; p < D; p++)
                    {
                        for (int c = 0; c < d; c++)
                        {
                            int roll = rng.Next(6);
                            A[p, c] = roll == 0 ? -1.0 : (roll == 5 ? 1.0 : 0.0);
                        }
                    }

                    double[,] Z = new double[N, d];
                    for (int i = 0; i < N; i++)
                    {
                        for (int c = 0; c < d; c++)
                        {
                            double sum = 0.0;
                            for (int p = 0; p < D; p++)
                                sum += X[i, p] * A[p, c];
                            Z[i, c] = scale * sum;
                        }
                    }

                    double[,] rhoZ = ComputeRho(Z, N, d);
                    double fZ = RawStress(rhoZ, delta, N);
                    double sZ = Math.Sqrt(fZ / sumDeltaSq);
                    double kZ = ConcentrationK(rhoZ, N);

                    sumS_Rp += sZ;
                    if (kZ == -1.0) hasMinusOne = true;
                    sumK_Rp += kZ;
                }

                double meanS_Rp = sumS_Rp / R;
                double meanK_Rp = hasMinusOne ? -1.0 : (sumK_Rp / R);

                if (minPca == -1 && cevr >= q) minPca = d;
                if (minMds == -1 && sMds <= epsMds) minMds = d;
                if (minRp == -1 && meanS_Rp <= epsRp) minRp = d;

                Console.WriteLine(string.Format(CultureInfo.InvariantCulture,
                    "{0} {1:F4} {2:F4} {3:F4} {4:F4} {5:F4} {6:F4} {7:F4}",
                    d, cevr, sPca, kPca, sMds, kMds, meanS_Rp, meanK_Rp));
            }

            Console.WriteLine($"Minima PCA={minPca} MDS={minMds} RP={minRp}");
        }
    }

    static double Distance(double[,] Z, int i, int j, int d)
    {
        double sum = 0.0;
        for (int k = 0; k < d; k++)
        {
            double diff = Z[i, k] - Z[j, k];
            sum += diff * diff;
        }
        return Math.Sqrt(sum);
    }

    static double[,] ComputeRho(double[,] Z, int N, int d)
    {
        double[,] rho = new double[N, N];
        for (int i = 0; i < N; i++)
        {
            for (int j = i + 1; j < N; j++)
            {
                rho[i, j] = rho[j, i] = Distance(Z, i, j, d);
            }
        }
        return rho;
    }

    static double RawStress(double[,] rho, double[,] delta, int N)
    {
        double f = 0.0;
        for (int i = 0; i < N; i++)
        {
            for (int j = i + 1; j < N; j++)
            {
                double diff = delta[i, j] - rho[i, j];
                f += diff * diff;
            }
        }
        return f;
    }

    static double ConcentrationK(double[,] rho, int N)
    {
        double minD = double.MaxValue;
        double maxD = 0.0;
        for (int i = 0; i < N; i++)
        {
            for (int j = i + 1; j < N; j++)
            {
                double dist = rho[i, j];
                if (dist < minD) minD = dist;
                if (dist > maxD) maxD = dist;
            }
        }
        if (maxD == 0.0) return -1.0;
        if (minD == 0.0) return 0.0;
        return minD / maxD;
    }

    static IEnumerable<string> Tokenize(TextReader reader)
    {
        int c;
        while ((c = reader.Read()) != -1)
        {
            if (char.IsWhiteSpace((char)c)) continue;
            var sb = new System.Text.StringBuilder();
            sb.Append((char)c);
            while ((c = reader.Read()) != -1 && !char.IsWhiteSpace((char)c))
                sb.Append((char)c);
            yield return sb.ToString();
        }
    }
}
