import media
import fresh_tomatoes

Pirates_of_the_Caribbean = media.Movie('Pirates of the Caribbean',
								   	   'http://cdn2-www.superherohype.com/assets/uploads/gallery/pirates-of-the-caribbean-dead-men-tell-no-tales/17015800_10154981836668830_529268610073059017_o.jpg',
									   'https://www.youtube.com/watch?v=lsJ58L3u8qw')

Big_Hero_6 = media.Movie('Big Hero 6',
						 'http://vignette2.wikia.nocookie.net/disney/images/8/89/Big_Hero_6_film_poster.jpg/revision/latest?cb=20160505193934',
						 'https://www.youtube.com/watch?v=rD5OA6sQ97M')

The_Imitation_Game = media.Movie('The Imitation Game',
								 'http://www.impawards.com/2014/posters/imitation_game_ver4_xlg.jpg',
								 'https://www.youtube.com/watch?v=S5CjKEFb-sM')

movie_list = [Pirates_of_the_Caribbean, Big_Hero_6, The_Imitation_Game]
fresh_tomatoes.open_movies_page(movie_list)