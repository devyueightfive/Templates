using System;
using System.Collections.Generic;
using System.Text;

namespace StrategySample
{
    public abstract class Strategy:IStrategyA
    {
        private IStrategyA behaviorA;

        public Strategy()
        {
            behaviorA = new UsualStrategyA();
        }

        public virtual void SetStrategyA(IStrategyA behavior)
        {
            behaviorA = behavior;
        }

        public virtual void ConcreateAlgorithmA()
        {
            behaviorA.ConcreateAlgorithmA();
        }

        public abstract void Display();

    }
}
