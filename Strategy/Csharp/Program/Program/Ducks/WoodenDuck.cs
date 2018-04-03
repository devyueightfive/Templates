using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Program
{
    class WoodenDuck:SimpleDuck
    {
        public WoodenDuck()
        {
            setFlyBehavior(new Fly.NoFly());
        }

        public override void Display()
        {
            Console.WriteLine("I'm wooden duck.");
        }
    }
}
