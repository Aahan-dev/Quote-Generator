import random

class QuoteGenerator:
    def __init__(self):
        """Initialize the QuoteGenerator with a list of quotes and jokes."""
        self.quotes = [
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Life is what happens when you're busy making other plans. - John Lennon",
            "The purpose of our lives is to be happy. - Dalai Lama",
            "Get busy living or get busy dying. - Stephen King",
            "You only live once, but if you do it right, once is enough. - Mae West"
        ]
        
        self.jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "What do you call fake spaghetti? An impasta!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you call cheese that isn't yours? Nacho cheese!",
            "Why did the bicycle fall over? Because it was two-tired!"
        ]

    def get_random_quote(self):
        """Return a random quote from the list of quotes."""
        return random.choice(self.quotes)

    def get_random_joke(self):
        """Return a random joke from the list of jokes."""
        return random.choice(self.jokes)

    def generate_quote_or_joke(self):
        """Randomly decide to return either a quote or a joke."""
        if random.choice([True, False]):
            return self.get_random_quote()
        else:
            return self.get_random_joke()

if __name__ == "__main__":
    # Create a QuoteGenerator instance
    generator = QuoteGenerator()
    
    # Generate and print a random quote or joke
    print(generator.generate_quote_or_joke())