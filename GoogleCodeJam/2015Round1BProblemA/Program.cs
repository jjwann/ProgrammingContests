using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Program
{
    public static void Main()
    {
        using (FileStream iStream = File.OpenRead(@"C:\Users\James\Downloads\input.in"))
        {
            using (FileStream oStream = File.OpenWrite(@"C:\Users\James\Documents\Visual Studio 2012\Projects\TopCoder\TopCoder\output.out"))
            {
                using (StreamReader sr = new StreamReader(iStream))
                {
                    int t = int.Parse(sr.ReadLine());
                    string o = "Case #{0}: ";

                    using (StreamWriter sw = new StreamWriter(oStream))
                    {
                        int e;
                        long n, r;

                        int[] d = new int[14];
                        d[0] = 10;

                        for (int i = 1; i < d.Length; i++)
                        {
                            d[i] = d[i - 1] + Calculate((long)Math.Pow(10, i + 1) - 1, i + 1) + 1;
                        }
                        
                        for (int i = 0; i < t; i++)
                        {
                            n = long.Parse(sr.ReadLine());

                            if (n < 10)
                            {
                                r = n;
                            }
                            else
                            {
                                e = 2;

                                while (n > Math.Pow(10, e))
                                    e++;

                                r = d[e - 2];

                                if (n != (long)Math.Pow(10, e - 1))
                                    r += n % 10 == 0 ? Calculate(n - 1, e) + 1 : Calculate(n, e);
                            }

                            sw.WriteLine(string.Format(o, i + 1) + r);
                        }
                    }
                }
            }
        }
    }

    private static int Calculate(long value, int places)
    {
        int r = 0;
        int h, a;
        
        h = places >> 1;
        a = 0;

        for (int j = 0; j < h; j++)
        {
            a += (int)(value % 10) * (int)Math.Pow(10, j);
            value /= 10;
        }

        r += a;

        if (places % 2 > 0)
        {
            r += (int)(value % 10) * (int)Math.Pow(10, h);
            value /= 10;
        }

        if (value != (int)Math.Pow(10, h - 1))
        {
            a = 0;
            for (int j = 0; j < h; j++)
            {
                a = a * 10 + (int)(value % 10);
                value /= 10;
            }

            r += a;
        }

        return r;
    }
}