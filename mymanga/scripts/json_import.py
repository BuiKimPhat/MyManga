import json
from manga.models import *
json_path = "E:\\School\\Python\\MyManga\\mymanga\\scripts\\manga_data.json"
with open(json_path, encoding='utf-8') as f:
    data = json.load(f)
for i,manga in enumerate(data):
    print(f"Saving manga {i+1}/{len(data)} {manga['name']}...")
    # Manga detail
    new_manga = Manga(id=manga["id"], 
                    name=manga["name"], 
                    thumbnail=manga["thumbnail"], 
                    status=manga["status"],
                    views=manga["views"],
                    chapters_number=manga["chapters_number"])
    new_manga.save()
    # Adding genres
    for genre in manga["genres"]:
        find_genre = Genre.objects.filter(name=genre.strip())
        if find_genre.count() == 0:
            new_genre = Genre(name=genre.strip())
            new_genre.save()
            new_manga.genres.add(new_genre)
        else:
            new_manga.genres.add(find_genre[0])
    new_chapters = []
    # Adding chapters
    for ii,chapter in enumerate(manga["chapters"]):
        print(f"Chapter {ii+1}/{len(manga['chapters'])}...")
        new_chapter = Chapter(id=chapter["id"],
                            name=chapter["name"],
                            modified_date=chapter["modified_date"].replace("\\n","").strip(),
                            views=chapter["views"],
                            manga=new_manga)
        new_chapters.append(new_chapter)
        new_contents = []
        # Adding contents
        for content in chapter["contents"]:
            new_content = Content(chapter=new_chapter,
                                index=content["index"],
                                link=content["link"])
            new_contents.append(new_content)
    Chapter.objects.bulk_create(new_chapters)
    Content.objects.bulk_create(new_contents)
print("Done!")