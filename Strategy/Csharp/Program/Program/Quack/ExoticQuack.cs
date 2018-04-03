using System;

namespace Program.Quack
{
    class ExoticQuack: IQuackable
    {
        public void Quack()
        {
            Console.WriteLine("Meow!Meow!");
        }
    }
}
