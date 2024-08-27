import { useState } from 'react';
import { FactBitT } from '/src/api/types/StepT';

const mockSteps = {
  id: 'root',
  fact: 'Root step',
  childSteps: [
    {
      id: '1',
      fact: 'The [alice@example.com:user] visits the [project:route]',
      childSteps: [
        {
          id: '1.1',
          fact: 'The [scenario-list-view:component] displays the scenarios',
          childSteps: [],
        },
      ],
    },
    {
      id: '2',
      fact: 'The [alice@example.com:user] clicks on the [my-first:scenario]',
      childSteps: [
        {
          id: '2.1',
          fact: 'The [step-tree-view:component] shows the root steps for the [my-first:scenario] in the [step-list-view:component]',
          childSteps: [],
        },
      ],
    },
    {
      id: '3',
      fact: 'The [alice@example.com:user] clicks on a root level step',
      childSteps: [
        {
          id: '3.1',
          fact: 'The [step-list-view:component] highlights the [base-step-1:step]',
          childSteps: [],
        },
        {
          id: '3.2',
          fact: 'The [step-tree-view:component] opens a new [step-list-view:component] to the right',
          childSteps: [],
        },
      ],
    },
  ],
};

const mockActors = {
  'alice@example.com:user': {
    id: 'user1',
    key: 'alice@example.com:user',
    fields: {
      email: 'alice@example.com',
      name: 'Alice',
    },
    changedFields: [],
  },
  'project:route': {
    id: 'route1',
    key: 'project:route',
    fields: {
      path: '/project/:id',
    },
    changedFields: [],
  },
  'my-first:scenario': {
    id: 'scenario1',
    key: 'my-first:scenario',
    fields: {
      name: 'My First Scenario',
      description: 'This is the first scenario in the project',
    },
    changedFields: [],
  },
  'base-step-1:step': {
    id: 'step1',
    key: 'base-step-1:step',
    fields: {
      fact: 'The [alice@example.com:user] clicks on a root level step',
    },
    changedFields: [],
  },
};

const Step = ({ step, depth = 0, onActorClick }: any) => {
  const [isExpanded, setIsExpanded] = useState(false);

  const toggleExpand = () => {
    setIsExpanded(!isExpanded);
  };

  const renderFactWithLinks = (fact: FactBitT[]) => {
    return fact.map((factBit: FactBitT, index: any) => {
      if (factBit.type === 'actor') {
        const actorKey = factBit.value;
        return (
          <span
            key={index}
            className="cursor-pointer text-blue-400 hover:underline"
            onClick={(e) => {
              e.stopPropagation();
              onActorClick(actorKey);
            }}
          >
            {actorKey}
          </span>
        );
      }
      return factBit.value;
    });
  };

  return (
    <div style={{ marginLeft: depth * 20 }}>
      <div
        onClick={toggleExpand}
        className="mb-2 flex cursor-pointer items-start"
      >
        <span className="mr-2 w-5 text-gray-400">
          {step.childSteps.length > 0 ? (isExpanded ? '▼' : '►') : '•'}
        </span>
        <div className="flex-1 break-words">
          {renderFactWithLinks(step.fact)}
        </div>
      </div>
      {isExpanded &&
        step.childSteps.map((childStep: any) => (
          <Step
            key={childStep.id}
            step={childStep}
            depth={depth + 1}
            onActorClick={onActorClick}
          />
        ))}
    </div>
  );
};

const ActorView = ({ actor }: any) => {
  if (!actor) return null;

  return (
    <div className="mt-6 rounded-lg border border-gray-700 bg-gray-800 p-4">
      <h3 className="mb-2 text-xl font-bold">Actor: {actor.key}</h3>
      <p>
        <strong>ID:</strong> {actor.id}
      </p>
      <h4 className="mb-2 mt-4 text-lg font-semibold">Fields:</h4>
      <ul className="space-y-1">
        {Object.entries(actor.fields).map(([key, value]) => (
          <li key={key}>
            <strong>{key}:</strong> {value}
            {actor.changedFields.includes(key) && (
              <span className="text-green-400 ml-2">(Changed)</span>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
};

export const MockStepTreeView = () => {
  const [selectedActor, setSelectedActor] = useState(null);

  const handleActorClick = (actorKey: any) => {
    setSelectedActor((mockActors as any)[actorKey]);
  };

  return (
    <div className="mx-auto max-w-3xl rounded-xl bg-gray-900 p-6 font-sans text-gray-100 shadow-lg">
      <h2 className="mb-6 text-2xl font-bold">Step Tree View</h2>
      <div className="rounded-lg bg-gray-800 p-4">
        <Step step={mockSteps} onActorClick={handleActorClick} />
      </div>
      <ActorView actor={selectedActor} />
    </div>
  );
};
