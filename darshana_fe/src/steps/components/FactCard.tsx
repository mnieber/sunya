import { StepT } from '/src/api/types/StepT';

type PropsT = {
  step: StepT;
  setHighlightedActor: (step: StepT, actorKey: string) => void;
};

export const Fact = (props: PropsT) => {
  return props.step.fact.map((factBit, index) => {
    if (factBit.typeName === 'actor' || factBit.typeName === 'role') {
      return (
        <span
          key={index}
          className="ml-1 cursor-pointer text-blue-400 hover:underline"
          onClick={(e) => {
            e.stopPropagation();
            props.setHighlightedActor(props.step, factBit.value);
          }}
        >
          {factBit.value}
        </span>
      );
    }
    return (
      <span className="ml-1" key={index}>
        {factBit.value}
      </span>
    );
  });
};
