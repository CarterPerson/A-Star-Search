clear;


generate(40,40, .2)

function returner = generate(row,col, odds)
    maze = "";
    for x = 1:col
        for y = 1:row
            num = rand();
            if num < odds
                maze = maze + "#";
            else
                maze = maze + ".";
            end
        end
        maze = maze + newline;
    end
    maze
    
end