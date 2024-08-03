import { initRS } from 'mobx-resource-states';
import { EntityT } from '/src/api/types/EntityT';
import { createUUID } from '/src/utils/ids';
import { ObjT } from '/src/utils/types';

export type BlogPostT = EntityT & {
  title: string;
  content: string | undefined;
  slug: string;
  isPublished: boolean;
  level: BlogPostLevelT;
  tags: string[];
};

export type BlogPostLevelT = 'easy' | 'medium' | 'hard';

export type BlogPostByIdT = { [id: string]: BlogPostT };

export const createBlogPost = (values: ObjT): BlogPostT => {
  return initRS({
    id: createUUID(),
    isTransient: true,
    title: 'New blog-post',
    slug: '-',
    content: values.content,
    isPublished: false,
    level: 'medium',
    tags: [],
  } as BlogPostT);
};

export const getBlogPostLevelOptions = (args: {}) => {
  return Promise.resolve([
    { value: 'easy', label: 'Easy' },
    { value: 'medium', label: 'Medium' },
    { value: 'hard', label: 'Hard' },
  ]);
};
