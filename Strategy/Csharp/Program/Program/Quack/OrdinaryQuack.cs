using System;

namespace Program.Quack
{
    class OrdinaryQuack : IQuackable
    {
        public void Quack()
        {
            Console.WriteLine("Quack! Quack!");
        }
    }
}
