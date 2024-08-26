import { observer } from 'mobx-react-lite';
import React from 'react';
import { withContextProps } from 'react-props-from-context';
import { StepT } from '/src/api/types/StepT';
import { stepTreeCtx } from '/src/steps/hooks/useStepTreeContext';
import { cn } from '/src/utils/classnames';

export type PropsT = {
  actorKey: string;
  step: StepT;
  className?: any;
};

const ContextProps = {
  stepTreeState: stepTreeCtx.stepTreeState,
};

export const ActorLink = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const handleClick = (e: React.MouseEvent) => {
      e.stopPropagation(); // Prevent the click from affecting parent elements (like expanding/collapsing steps)
      // stepTreeState.actionsCtr.setHighlightedActor(actorKey, props.step);
    };

    return (
      <span
        className={cn(
          'ActorLink',
          'cursor-pointer text-blue-400 hover:text-blue-300',
          props.className
        )}
        onClick={handleClick}
      >
        {props.actorKey}
      </span>
    );
  }, ContextProps)
);
