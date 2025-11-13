import classnames from 'classnames';
import { formatDistanceToNow } from 'date-fns';
import mergeProps from 'merge-props';
import { observer } from 'mobx-react-lite';
import { isUpdating } from 'mobx-resource-states';
import React from 'react';
import { selectionUIHandlers, SelectionUIPropsT } from 'skandha-facets';
import './AtlasBriefsListViewItem.scss';
import { AtlasBriefT } from '/src/api/types';
import { atlasesNav } from '/src/atlases/routes';
import { L } from '/src/frames/layout';
import { navTo } from '/src/routes/navHandler';

export type PropsT = {
  atlasBrief: AtlasBriefT;
  className?: any;
  selectionUIProps: SelectionUIPropsT;
};

export const AtlasBriefsListViewItem: React.FC<PropsT> = observer(
  (props: PropsT) => {
    const formattedDate = props.atlasBrief.createdAt.toLocaleDateString();
    const age = formatDistanceToNow(props.atlasBrief.createdAt, {
      addSuffix: true,
    });
    const atlasRouteSpec = atlasesNav.atlas({
      atlasId: props.atlasBrief.id,
    });

    return (
      <a
        className={classnames(
          'AtlasBriefsListViewItem',
          L.row.bar(),
          { 'animate-delete': isUpdating(props.atlasBrief) },
          props.className
        )}
        href={atlasRouteSpec.url}
        {...mergeProps(selectionUIHandlers(props.selectionUIProps), {
          onClick: (e: React.MouseEvent<HTMLAnchorElement>) => {
            if (!(e.ctrlKey || e.shiftKey)) {
              e.preventDefault();
              navTo(atlasRouteSpec);
            }
          },
        })}
      >
        <div className="flex items-center gap-3 flex-1">
          <span className="AtlasBriefsListViewItem__date">{formattedDate}</span>
          {props.atlasBrief.isSyncedWithJira && (
            <span className="AtlasBriefsListViewItem__icon">✔</span>
          )}
        </div>
        <div className="flex items-center flex-1">
          <span className="AtlasBriefsListViewItem__age">{age}</span>
        </div>
      </a>
    );
  }
);
