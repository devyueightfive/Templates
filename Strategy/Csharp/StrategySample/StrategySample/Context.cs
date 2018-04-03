using System;
using System.Collections.Generic;
using System.Text;

namespace StrategySample
{
    class Context : Strategy
    {
        public override void Display()
        {
            Console.WriteLine("It' s Context.");
        }
    }
}
