import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]

def average_rating(movies) -> float:
    if not movies:
        return 0.0
    total = sum(m["rating"] for m in movies)
    return round(total / len(movies), 1)
def catalog_age_stats(movies, current_year=2026) -> tuple:
    if not movies:
        return (0, 0, 0)
    ages = [current_year - m["year"] for m in movies]
    return (max(ages), min(ages), math.ceil(sum(ages) / len(ages)))

def duration_in_hours(minutes: int) -> str:
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"

def rating_tier(rating: float) -> str:
    is_masterpiece = True if rating >= 9 else False
    if is_masterpiece:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    elif rating >= 5:
        return "средне"
    else:
        return "слабо"
def decade_label(year: int) -> str:
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"

def print_non_comedy(movies: list) -> None:
    print("\nФильмы не в жанре комедия")
    for m in movies:
        if "comedy" in m["genres"]:
            continue
        print(m["title"])

def find_first_masterpiece(movies: list) -> None:
    print("\nПоиск первого шедевра")
    i = 0
    while i < len(movies):
        if movies[i]["rating"] > 9.0:
            print(f"Найден шедевр: {movies[i]['title']} ({movies[i]['rating']})")
            break
        i += 1
    else:
        print("Шедевров не найдено")

def count_long_movies(movies: list, threshold: int = 120) -> int:
    count = 0
    for m in movies:
        if m["duration_min"] > threshold:
            count += 1
    return count

def normalize_title(title: str) -> str:
    words = title.split()
    new_words = []
    for w in words:
        new_words.append(w[0].upper() + w[1:])
    return " ".join(new_words)

def make_slug(title: str) -> str:
    return normalize_title(title).lower().replace(" ", "-")

def format_report_line(movie: dict) -> str:
    dur = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return (
        f'"{movie["title"]}" ({movie["year"]}) — {movie["rating"]}/10,'
        f'{dur}, жанры: {genres}'
    )
def titles_sorted_by_rating(movies: list) -> list:
    sorted_m = sorted(movies, key=lambda x: x["rating"], reverse=True)
    return [m["title"] for m in sorted_m]

def top_n_by_rating(movies: list, n: int = 3) -> list:
    sorted_m = sorted(movies, key=lambda x: x["rating"], reverse=True)
    return [(m["title"], m["rating"]) for m in sorted_m[:n]]

def count_by_genre(movies: list) -> dict:
    counts = {}
    for m in movies:
        for g in m["genres"]:
            counts[g] = counts.get(g, 0) + 1
    return counts

def actor_filmography(movies: list) -> dict:
    actors = {}
    for m in movies:
        for a in m["actors"]:
            if a not in actors:
                actors[a] = []
            actors[a].append(m["title"])
    return actors

def high_rated_movies(movies: list) -> dict:
    avg = average_rating(movies)
    return {m["title"]: m["rating"] for m in movies if m["rating"] > avg}

def all_genres(movies: list) -> set:
    genres = set()
    for m in movies:
        genres |= m["genres"] 
    return genres

def common_actors(movie1: dict, movie2: dict) -> set:
    return set(movie1["actors"]) & set(movie2["actors"])

def genres_only_in_one(movies_a: list, movies_b: list) -> set:
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)
    return genres_a - genres_b

def iter_high_rated(movies: list, min_rating: float = 8.0):
    for m in movies:
        if m["rating"] >= min_rating:
            yield m

def build_report(movies: list) -> None:
    print("\nОТЧЕТ ПО КАТАЛОГУ")
    
    print(f"Средний рейтинг:{average_rating(movies)}")
    
    age_stats = catalog_age_stats(movies)
    print(f"Средний возраст фильмов:{age_stats[2]} лет")
    
    print("\nТоп-3 фильма:")
    top = top_n_by_rating(movies, 3)
    for title, rating in top:
        for m in movies:
            if m["title"] == title:
                print(f"  {format_report_line(m)}")
                break
        
    print("\nФильмов по жанрам:")
    counts = count_by_genre(movies)
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    for genre, count in sorted_counts:
        print(f"  {genre} — {count}")
        
    all_g = all_genres(movies)
    print(f"\nВсе жанры каталога: {', '.join(sorted(all_g))}")

def main() -> None:
    build_report(movies)

if __name__ == "__main__":
    main()