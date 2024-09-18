export const breakpoints = {
  xs: '320px',
  small: '480px',
  medium: '768px',
  large: '976px',
  xlarge: '1280px',
};

export const L = {
  box: (h: string, w: string) => `flex ${h} ${w}`,
  row: {
    canvas: () => 'flex grow flex-row',
    bar: () => 'flex flex-row',
    barRev: () => 'flex flex-row items-end',
    skewer: () => 'flex flex-row items-center',
    skewerRev: () => 'flex flex-row items-center items-end',
    banner: () => 'flex grow flex-row items-stretch',
    bannerRev: () => 'flex grow flex-row items-stretch items-end',
    flagPole: () => 'flex flex-row items-start',
    revFlagPole: () => 'flex flex-row items-end',
  },
  col: {
    canvas: () => 'flex grow flex-col',
    bar: () => 'flex flex-col',
    barRev: () => 'flex flex-col items-end',
    skewer: () => 'flex flex-col items-center',
    skewerRev: () => 'flex flex-col items-center items-end',
    banner: () => 'flex grow flex-col items-stretch',
    bannerRev: () => 'flex grow flex-col items-stretch items-end',
    flagPole: () => 'flex flex-col items-start',
    flagPoleRev: () => 'flex flex-col items-end',
  },
};
