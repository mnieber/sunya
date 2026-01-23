import sunya
from sunya import M as m
from sunya import R as r
from sunya import Rel as rel
from sunya import actions as a
from sunya import actor, goal, note_over, participant, self

scenario = sunya.add_scenario(f"ms1_a_user_creates_a_book")
markdown_node = sunya.add_markdown_node(scenario, "A user creates a book")

markdown_node.markdown = f"""
```mermaid
sequenceDiagram
    {actor(m.External.Actors.User                    , role=r.User)}
    {participant(m.Books.Actions.CreateBook          , role=r.CreateBookAction)}
    {participant(m.Chapters.Actions.CreateChapter    , role=r.CreateChapterAction)}
    {participant(m.Chapters.Actions.CreateParagraph  , role=r.CreateParagraphAction)}
    {participant(m.Chapters.Rules.IsBadWord          , role=r.IsBadWordRule)}

    # 🔳 Create book
    {note_over(r.User, goal(rel().create_a(r.book).with_lorem_ipsum_text()))}
    {r.User                   >  r.User}                   : {a.it(rel().prepares_a(r.create_book_form))}
    {r.User                   >  r.CreateBookAction}       : {a.calls(create_book_form=r.create_book_form)}
    {r.CreateBookAction       >> self()}                   : {a.creates(r.book)}

    # 🔳 Create chapters
    loop for each chapter (3 times)
        {r.CreateBookAction   >> r.CreateBookAction}       : {a.it(rel().prepares_a(r.create_chapter_form))}
        {r.CreateBookAction   >> r.CreateChapterAction}    : {a.calls(book=r.book, create_chapter_form=r.create_chapter_form)}
        {r.CreateChapterAction >> self()}                  : {a.creates(r.chapter)}

        # 🔳 Create paragraphs
        loop for each paragraph that must be created
            {r.CreateChapterAction >> r.CreateParagraphAction} : {a.calls()}
            {r.CreateParagraphAction >> self()}                : {a.creates(r.paragraph).with_lorem_ipsum_text()}
            {note_over(r.CreateParagraphAction, "Counts bad words (words containing 'a' or 'b')")}
            {r.CreateParagraphAction >> self()}                : {a.it(rel().filters(r.paragraph).to_have_at_most_N(r.bad_words))}
            {r.CreateParagraphAction >> r.IsBadWordRule}       : {a.calls()}
            {r.CreateParagraphAction >> self()}                : {a.it(rel().adds(r.paragraph).to(r.chapter))}
            {r.CreateParagraphAction >> r.CreateChapterAction} : {a.returns(r.paragraph)}
        end

        {r.CreateChapterAction >> self()}                  : {a.it(rel().adds(r.chapter).to(r.book))}
        {r.CreateChapterAction >> r.CreateBookAction}      : {a.returns(r.chapter)}
    end

    {r.CreateBookAction       >> r.User}                   : {a.returns(r.book)}
```
"""
