##
## EPITECH PROJECT, 2023
## B-MAT-200-BDX-2-1-106bombyx-elliot.masina
## File description:
## Makefile
##

SRC			=		src/

NAME		=		106bombyx

all:				$(SRC)
					@cp $(SRC)main.py $(NAME)
					@chmod +x $(NAME)

clean:
					rm -rf $(NAME)

fclean:				clean

re:					fclean all

.PHONY:				all clean fclean re
