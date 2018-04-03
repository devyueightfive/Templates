using System;
using System.Collections.Generic;
using System.Text;

namespace StrategySample
{
    class StrategyB : IStrategyB
    {
        public void ConcreateAlgorithmB()
        {
            Console.WriteLine("Algorithm B");
        }
    }
}
