import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { atlasCtx } from '/src/atlases/hooks/useAtlasContext';

// Import styles
import './AtlasHeader.scss';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  atlas: atlasCtx.filteredAtlas,
};

export const AtlasHeader = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    if (!props.atlas) {
      return null;
    }

    return (
      <div className="AtlasHeader">
        <div className="AtlasHeader__meta">
          <span className="AtlasHeader__date">
            {props.atlas.createdAt.toLocaleDateString('en-US', {
              year: 'numeric',
              month: 'long',
              day: 'numeric',
            })}
          </span>
          {props.atlas.isSyncedWithJira && (
            <span className="AtlasHeader__sync-badge">Synced with Jira</span>
          )}
        </div>
      </div>
    );
  }, ContextProps)
);
