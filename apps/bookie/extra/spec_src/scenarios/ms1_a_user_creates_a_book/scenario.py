import sunya
from sunya import (
    goal,
    M as m,
    R as r,
    Rel as rel,
    actions as a,
    self,
    participant,
    actor,
    note_over,
)

scenario = sunya.add_scenario(f"ms1_a_user_creates_a_book")
markdown_node = sunya.add_markdown_node(scenario, "A user creates a book")

markdown_node.markdown = f"""
```mermaid
sequenceDiagram
    {actor(m.External.Actors.User                    , role=r.User)}
    {participant(m.Books.Actions.CreateBook          , role=r.CreateBookAction)}
    {participant(m.Chapters.Actions.CreateChapter    , role=r.CreateChapterAction)}
    {participant(m.Chapters.Actions.CreateParagraph  , role=r.CreateParagraphAction)}

    # 🔳 Create book
    {note_over(r.User, goal(rel().create_a(r.book).with_lorem_ipsum_text()))}
    {r.User                   >  r.CreateBookAction}       : {a.calls(title="My Book", num_chapters=3)}
    {r.CreateBookAction       >> self()}                   : {a.creates(r.book)}

    # 🔳 Create chapters
    loop for each chapter (3 times)
        {r.CreateBookAction   >> r.CreateChapterAction}    : {a.calls()}
        {r.CreateChapterAction >> self()}                  : {a.creates(r.chapter)}

        # 🔳 Create paragraphs
        loop for each paragraph (5 times)
            {r.CreateChapterAction >> r.CreateParagraphAction} : {a.calls()}
            {r.CreateParagraphAction >> self()}                : {a.creates(r.paragraph)}
            {r.CreateParagraphAction >> self()}                : {a.it(rel().adds(r.paragraph).to(r.chapter))}
            {r.CreateParagraphAction >> r.CreateChapterAction} : {a.returns(r.paragraph)}
        end

        {r.CreateChapterAction >> self()}                  : {a.it(rel().adds(r.chapter).to(r.book))}
        {r.CreateChapterAction >> r.CreateBookAction}      : {a.returns(r.chapter)}
    end

    {r.CreateBookAction       >> r.User}                   : {a.returns(r.book)}
```
"""
