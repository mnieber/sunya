import { observer } from 'mobx-react-lite';
import * as R from 'ramda';
import React from 'react';
import { withContextProps } from 'react-props-from-context';
import { useParams } from 'wouter';
import { AtlasBriefT } from '/src/api/types';
import { atlasBriefsCtx } from '/src/atlases/hooks/useAtlasBriefsContext';
import { useRefUrl } from '/src/routes/hooks/useRefUrl';
import { UrlEffectView } from '/src/utils/components';
import { ObjT } from '/src/utils/types';

type PropsT = {};

const ContextProps = {
  atlasBriefs: atlasBriefsCtx.atlasBriefs,
  atlasBrief: atlasBriefsCtx.atlasBrief,
  atlasBriefsSelection: atlasBriefsCtx.atlasBriefsSelection,
};

export const SelectAtlasBriefEffect = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const params = useParams() as ObjT;
    const { updateRefUrl, hasUrlChanged } = useRefUrl();

    const { atlasBriefsSelection, atlasBrief, atlasBriefs } = props;
    const atlasBriefFromUrl = R.find(
      (x: AtlasBriefT) => x.id === params.atlasId
    )(atlasBriefs);
    const isAtlasBriefInSyncWithUrl = atlasBrief?.id === atlasBriefFromUrl?.id;

    const selectAtlasBrief = (atlasBrief?: AtlasBriefT) => {
      atlasBriefsSelection.selectItem({ itemId: atlasBrief?.id });
    };

    React.useEffect(() => {
      // If there is a new url
      if (hasUrlChanged) {
        if (atlasBriefFromUrl) {
          updateRefUrl();
          if (!isAtlasBriefInSyncWithUrl) {
            selectAtlasBrief(atlasBriefFromUrl);
          }
        } else {
          selectAtlasBrief(undefined);
        }
      }
    });

    return (
      <UrlEffectView
        resourceName="atlasBrief"
        isInSync={isAtlasBriefInSyncWithUrl}
        className="absolute"
      />
    );
  }, ContextProps)
);
