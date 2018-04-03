using Program.Quack;

namespace Program
{
    class ExoticDuck: SimpleDuck
    {
        public ExoticDuck()
        {
            setQuackBehavior(new Quack.ExoticQuack());
        }
    }
}
