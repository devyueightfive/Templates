using System;
using System.Collections.Generic;
using System.Text;

namespace StrategySample
{
    class StrategyA : IStrategyA
    {
        public void ConcreateAlgorithmA()
        {
            Console.WriteLine("Algorithm A");
        }
    }

    class UsualStrategyA : IStrategyA
    {
        public void ConcreateAlgorithmA()
        {
            Console.WriteLine("Algorithm usual A");
        }
    }
}
