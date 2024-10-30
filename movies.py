from pydantic import BaseModel, Field
import ell

class Actor(BaseModel):
    name: str = Field(description="Actor name")

class MovieReview(BaseModel):
    title: str = Field(description="The title of the movie")
    rating: int = Field(description="The rating of the movie out of 10")
    summary: str = Field(description="A brief summary of the movie")
    cast: list[Actor] = Field(default_factory=list, description="List of cast members of the movie")

@ell.complex(model="gpt-4o", response_format=MovieReview)
def generate_movie_review(movie: str) -> MovieReview:
    """You are a movie review generator. Given the name of a movie, you need to return a structured review."""
    return f"""
    Generate a movie review for '{movie}' in the following format:
    - Title: The exact movie title
    - Rating: A number from 1 to 10
    - Summary: A brief summary of the movie (2-3 sentences)
    - Cast: A list of 3-5 main actors in the movie
    """
    
    
# Add this debug function
def print_review_debug(review):
    print("Debug: MovieReview object contents:")
    print(f"Title: {review.title}")
    print(f"Rating: {review.rating}")
    print(f"Summary: {review.summary}")
    print(f"Cast: {review.cast}")
    print(f"Cast type: {type(review.cast)}")