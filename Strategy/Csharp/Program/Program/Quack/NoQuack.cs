using System;

namespace Program.Quack
{
    public class NoQuack: IQuackable
    {
        public void Quack()
        {
            Console.WriteLine("...");
        }
    }
}
