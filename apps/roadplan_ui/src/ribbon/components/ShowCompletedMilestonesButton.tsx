import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { atlasCtx } from '/src/atlases/hooks/useAtlasContext';
import { ToolButton } from '/src/frames/components/ToolButton';
import { ModestToolButtonTrim } from '/src/frames/components/ToolButton';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  atlasFiltering: atlasCtx.atlasFiltering,
};

export const ShowCompletedMilestonesButton = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    return (
      <ToolButton
        className={props.className}
        trim={ModestToolButtonTrim}
        iconName={props.atlasFiltering.showCompletedMilestones ? 'checkFilled' : 'checkEmpty'}
        label="Completed"
        onClick={() => props.atlasFiltering.toggleShowCompletedMilestones({})}
      />
    );
  }, ContextProps)
);
