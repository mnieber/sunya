import { StepT } from '/src/api/types/StepT';

type PropsT = {
  step: StepT;
  setHighlightedActor: (step: StepT, actorKey: string) => void;
};

export const FactCard = (props: PropsT) => {
  return props.step.fact.map((factBit, index) => {
    const prefix =
      index === 0 && props.step.typeName === 'goal' ? (
        <span className="font-bold">Goal: </span>
      ) : (
        ''
      );
    if (factBit.typeName === 'actor' || factBit.typeName === 'role') {
      return (
        <span
          key={index}
          className="ml-1 cursor-pointer text-blue-300 hover:underline"
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
      <span className="ml-1 text-gray-text" key={index}>
        {prefix}
        {factBit.value}
      </span>
    );
  });
};
