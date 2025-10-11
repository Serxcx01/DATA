pos_droped = 3
b = getBot()


local pos_x, pos_y = nil, nil
for _, t in pairs(getTiles()) do
  if t.fg == pos_droped or t.bg == pos_droped then
    pos_x, pos_y = t.x, t.y
    break
  end
end

if pos_x and pos_y then
  b:findPath(pos_x, pos_y)
else
  print("Tile drop tidak ditemukan")
end
