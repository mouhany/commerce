# Commerce
### [Video Demo](https://www.youtube.com/watch?v=CA5mGlBlIX0)
### Description: An eBay-like e-commerce auction site that will allow users to post auction listings, place bids on listings, comment on those listings, and add listings to a “watchlist.” Project built with Django.

# Specification
1. Log in and register user.
![Login page](./static/user_login.png)
![Register page](./static/user_register.png)
2. Create Listing: Users should be able to visit a page to create a new listing. They should be able to specify a title for the listing, a text-based description, and what the starting bid should be. Users should also optionally be able to provide a URL for an image for the listing and/or a category (e.g. Fashion, Toys, Electronics, Home, etc.).
![Create listing](./static/listings_create.png)
3. Active Listing Page: The default route of your web application should let users view all of the currently active auction listings. For each active listing, this page should display (at minimum) the title, description, current price, and photo (if one exists for the listing).
![Active listing](./static/listings_active.png)
![All listing](./static/listings_all.png)
![Closed listing](./static/listings_closed.png)
4. Listing Page: Clicking on a listing should take users to a page specific to that listing. On that page, users should be able to view all details about the listing, including the current price for the listing. 
![Listing](./static/listing.png)
![Comment](./static/listing_comment.png)
    - If the user is signed in, the user should be able to add the item to their “Watchlist.” If the item is already on the watchlist, the user should be able to remove it.
    - If the user is signed in, the user should be able to bid on the item. The bid must be at least as large as the starting bid, and must be greater than any other bids that have been placed (if any). If the bid doesn’t meet those criteria, the user should be presented with an error.
    - If the user is signed in and is the one who created the listing, the user should have the ability to “close” the auction from this page, which makes the highest bidder the winner of the auction and makes the listing no longer active.
    - If a user is signed in on a closed listing page, and the user has won that auction, the page should say so.
Users who are signed in should be able to add comments to the listing page. The listing page should display all comments that have been made on the listing.
5. Watchlist: Users who are signed in should be able to visit a Watchlist page, which should display all of the listings that a user has added to their watchlist. Clicking on any of those listings should take the user to that listing’s page.
![Watchlist](./static/listings_watchlist.png)
6. Categories: Users should be able to visit a page that displays a list of all listing categories. Clicking on the name of any category should take the user to a page that displays all of the active listings in that category.
![Categories](./static/listings_categories.png)
![Category](./static/listings_categories2.png)