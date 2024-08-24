import React from 'react';

const mockSteps = {
  id: 'root',
  fact: 'Root step',
  childSteps: [
    {
      id: '1',
      fact: 'The user visits the project page to view available scenarios',
      childSteps: [
        {
          id: '1.1',
          fact: 'The scenario list is displayed, showing all scenarios associated with the current project',
          childSteps: [],
        },
        {
          id: '1.2',
          fact: 'The user can see basic information about each scenario, such as its name and a brief description',
          childSteps: [],
        },
      ],
    },
    {
      id: '2',
      fact: 'The user selects a specific scenario to view its details',
      childSteps: [
        {
          id: '2.1',
          fact: 'The step tree view is initialized, showing the root-level steps of the selected scenario',
          childSteps: [],
        },
        {
          id: '2.2',
          fact: 'Each step in the tree view is initially collapsed to show only its fact',
          childSteps: [],
        },
      ],
    },
    {
      id: '3',
      fact: 'The user interacts with the step tree view to explore the scenario structure',
      childSteps: [
        {
          id: '3.1',
          fact: 'The user can expand or collapse individual steps to show or hide their child steps',
          childSteps: [],
        },
        {
          id: '3.2',
          fact: 'When a step is selected, more detailed information about that step is displayed in a separate view',
          childSteps: [],
        },
      ],
    },
  ],
};

const Step = ({ step, depth = 0 }: any) => {
  const [isExpanded, setIsExpanded] = React.useState(false);

  const toggleExpand = () => {
    setIsExpanded(!isExpanded);
  };

  return (
    <div style={{ marginLeft: `${depth * 20}px` }}>
      <div
        onClick={toggleExpand}
        style={{
          cursor: 'pointer',
          display: 'flex',
          alignItems: 'flex-start',
          marginBottom: '8px',
        }}
      >
        <span style={{ marginRight: '8px', minWidth: '20px' }}>
          {step.childSteps.length > 0 ? (isExpanded ? '▼' : '►') : '•'}
        </span>
        <div
          style={{
            flex: 1,
            wordWrap: 'break-word',
            overflowWrap: 'break-word',
          }}
        >
          {step.fact}
        </div>
      </div>
      {isExpanded &&
        step.childSteps.map((childStep: any) => (
          <Step key={childStep.id} step={childStep} depth={depth + 1} />
        ))}
    </div>
  );
};

export const MockStepTreeView = () => {
  return (
    <div
      style={{
        fontFamily: 'Arial, sans-serif',
        maxWidth: '600px',
        margin: '0 auto',
        padding: '20px',
        border: '1px solid #ccc',
        borderRadius: '5px',
      }}
    >
      <h2 style={{ marginBottom: '20px' }}>Step Tree View</h2>
      <Step step={mockSteps} />
    </div>
  );
};
