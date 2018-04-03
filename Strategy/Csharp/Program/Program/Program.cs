using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Program
{
    class Program
    {
        static void Main(string[] args)
        {
            SimpleDuck simple = new SimpleDuck();
            simple.Display();
            simple.Swim();
            simple.Quack();
            simple.Fly();
            Console.WriteLine();

            GreenDuck green = new GreenDuck();
            green.Display();
            green.Swim();
            green.Quack();
            green.Fly();
            Console.WriteLine();

            WoodenDuck wood = new WoodenDuck();
            wood.Display();
            wood.Swim();
            wood.Quack();
            wood.Fly();
            Console.ReadLine();

            ExoticDuck exotic = new ExoticDuck();
            exotic.Display();
            exotic.Swim();
            exotic.Quack();
            exotic.Fly();
            Console.ReadLine();

        }
    }
}
