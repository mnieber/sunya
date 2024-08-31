import { L } from '/src/frames/layout';

export const CardS = {
  layout: {
    default: () => L.col.banner(),
  },
  colours: {
    default: () => 'bg-gray-800',
  },
  padding: {
    medium: () => 'p-4 rounded-lg',
  },
  border: {
    none: () => '',
    default: () => 'border border-gray-600',
  },
};

export type CardTrimT = {
  base: {
    componentName: string;
    root: {
      layout: any;
      colours: any;
      padding: any;
      border: any;
    };
  };
};

export const DefaultCardTrim: CardTrimT = {
  base: {
    componentName: 'Card',
    root: {
      layout: CardS.layout.default(),
      colours: CardS.colours.default(),
      padding: CardS.padding.medium(),
      border: CardS.border.none(),
    },
  },
};
