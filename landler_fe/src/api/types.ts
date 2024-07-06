export type EntityT = {
  id: string;
};

export type BlogPostT = EntityT & {
  name: string;
  state: string;
};

export type BlogPostByIdT = { [id: string]: BlogPostT };
