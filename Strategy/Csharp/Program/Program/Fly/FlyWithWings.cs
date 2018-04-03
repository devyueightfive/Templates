using System;

namespace Program.Fly
{
    class FlyWithWings : IFlyable
    {
        public void Fly()
        {
            Console.WriteLine("I'm flying with Wings.");
        }
    }
}
