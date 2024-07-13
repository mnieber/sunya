import { EntityT } from '/src/api/types/EntityT';

export type BlogPostT = EntityT & {
  title: string;
  slug: string;
  isPublished: boolean;
};

export type BlogPostByIdT = { [id: string]: BlogPostT };
