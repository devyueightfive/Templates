using System;

namespace Program.Fly
{
    class NoFly: IFlyable
    {
        public void Fly()
        {
            Console.WriteLine("---");
        }
    }
}
