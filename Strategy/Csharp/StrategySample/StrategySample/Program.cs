using System;

namespace StrategySample
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Context c = new Context();
            c.Display();
            c.ConcreateAlgorithmA();
            c.SetStrategyA(new StrategyA());
            c.ConcreateAlgorithmA();
            c.SetStrategyA(new UsualStrategyA());
            c.ConcreateAlgorithmA();

            Console.WriteLine();
            Console.ReadKey();
        }
    }
}
