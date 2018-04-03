using System;
using Program.Fly;
using Program.Quack;

namespace Program
{
    public class SimpleDuck : IQuackable, IFlyable
    {
        private IQuackable quackBehavior;
        private IFlyable flyBehavior;

        public SimpleDuck()
        {
            quackBehavior = new OrdinaryQuack();
            flyBehavior = new FlyWithWings();
        }

        public virtual void Display()
        {
            Console.WriteLine("I'm a simple duck");
        }
        public void Swim()
        {
            Console.WriteLine("I'm swimming");
        }

        public void setFlyBehavior(IFlyable fly)
        {
            flyBehavior = fly;
        }

        public void setQuackBehavior(IQuackable quack)
        {
            quackBehavior = quack;
        }

        public void Fly()
        {
            flyBehavior.Fly();
        }

        public void Quack()
        {
            quackBehavior.Quack();
        }
    }
}
