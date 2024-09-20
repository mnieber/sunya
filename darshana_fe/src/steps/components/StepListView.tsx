import { observer } from 'mobx-react-lite';
import { useState } from 'react';
import { StepT } from '/src/api/types/StepT';
import { FactCard } from '/src/steps/components/FactCard';
import { cn } from '/src/utils/classnames';

type PropsT = {
  step: StepT;
  depth: number;
  setHighlightedActor: (step: StepT, actorKey: string) => void;
};

export const StepListView = observer((props: PropsT) => {
  const [isExpanded, setIsExpanded] = useState(true);

  const toggleExpand = () => {
    setIsExpanded(!isExpanded);
  };

  const hasFact = props.step.fact.length > 0;

  return (
    <div className={cn({ 'ml-7': props.depth > 1, 'ml-0': props.depth <= 1 })}>
      {hasFact && (
        <div
          onClick={toggleExpand}
          className="mb-2 flex cursor-pointer items-start"
        >
          <span className="mr-2 w-5 text-gray-400">
            {props.step.childSteps.length > 0 ? (isExpanded ? '▼' : '►') : '•'}
          </span>
          <div className="flex-1 break-words">
            <FactCard
              step={props.step}
              setHighlightedActor={props.setHighlightedActor}
            />
          </div>
        </div>
      )}
      {(!hasFact || isExpanded) &&
        props.step.childSteps.map((childStep) => (
          <StepListView
            key={childStep.id}
            step={childStep}
            depth={(props.depth ?? 0) + 1}
            setHighlightedActor={props.setHighlightedActor}
          />
        ))}
    </div>
  );
});
