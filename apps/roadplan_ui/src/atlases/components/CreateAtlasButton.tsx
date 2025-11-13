import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { useLocation } from 'wouter';
import { atlasesCtx } from '/src/atlases/hooks/useAtlasesContext';
import { atlasesNav } from '/src/atlases/routes';
import { ToolButton } from '/src/frames/components/ToolButton';
import { ModestToolButtonTrim } from '/src/frames/components/ToolButton';
import { navTo } from '/src/routes/navHandler';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  atlasesState: atlasesCtx.atlasesState,
  isCreatingAtlas: atlasesCtx.isCreatingAtlas,
};

export const CreateAtlasButton = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const [location] = useLocation();
    const isOnAtlasView = location.includes('/atlases/');

    const handleCreateAtlas = () => {
      props.atlasesState
        .createAtlas()
        .then((response: any) => {
          if (isOnAtlasView && response?.id) {
            navTo(
              atlasesNav.atlas({
                atlasId: response.id,
              })
            );
          }
        })
        .catch((error: any) => {
          console.error('Failed to create atlas:', error);
        });
    };

    return (
      <ToolButton
        className={props.className}
        trim={ModestToolButtonTrim}
        isUpdating={props.isCreatingAtlas}
        iconName="plus"
        label="Create Atlas"
        onClick={handleCreateAtlas}
      />
    );
  }, ContextProps)
);
