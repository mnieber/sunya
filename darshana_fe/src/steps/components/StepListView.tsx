import { observer } from 'mobx-react-lite';
import { useState } from 'react';
import { ActorLink } from '/src/actors/components/ActorLink';
import { StepT } from '/src/api/types/StepT';
import { cn } from '/src/utils/classnames';

export type PropsT = {
  step: StepT;
  className?: any;
  depth?: number;
};

export const StepListView = observer((props: PropsT) => {
  const { step, className, depth = 0 } = props;
  const [isExpanded, setIsExpanded] = useState(false);

  const toggleExpand = () => {
    setIsExpanded(!isExpanded);
  };

  const renderFactWithLinks = (step: StepT) => {
    const parts = step.fact.split(/(\[[^\]]+\])/);
    return parts.map((part, index) => {
      if (part.startsWith('[') && part.endsWith(']')) {
        const actorKey = part.slice(1, -1);
        return <ActorLink key={index} actorKey={actorKey} step={step} />;
      }
      return part;
    });
  };

  return (
    <div className={cn('StepListView', className)}>
      <div
        className={cn(
          'flex cursor-pointer items-start rounded p-2 hover:bg-gray-700',
          { 'bg-gray-700': isExpanded }
        )}
        onClick={toggleExpand}
        style={{ marginLeft: `${depth * 20}px` }}
      >
        <span className="mr-2 w-4 text-gray-400">
          {step.childSteps.length > 0 ? (isExpanded ? '▼' : '►') : '•'}
        </span>
        <div className="flex-1 text-gray-200">{renderFactWithLinks(step)}</div>
      </div>
      {isExpanded &&
        step.childSteps.map((childStep, index) => (
          <StepListView
            key={childStep.id || index}
            step={childStep}
            depth={depth + 1}
          />
        ))}
    </div>
  );
});
