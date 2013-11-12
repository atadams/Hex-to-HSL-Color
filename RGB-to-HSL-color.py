import sublime
import sublime_plugin
import re
import string



class RgbToHslCommand(sublime_plugin.TextCommand):

	def run(self, edit, convert_all = False, force_alpha = False):
		self.edit = edit

		if convert_all:
			selection = self.view.find_all('(#(?:[\da-f]{3}){1,2}(?![\da-f])|rgba?\(([\d, \%\.]+)\))', sublime.IGNORECASE)
			selection = reversed(selection)
		else:
			selection = self.view.sel()
		for region in selection:
			if not region.empty():
				word = self.view.substr(region)
				css_hsl = convert_to_hsl(word,force_alpha)
				if isinstance(css_hsl, str):
					self.view.replace(self.edit, region, css_hsl)



def convert_to_hsl(word,force_alpha = False):

	hex_re = re.compile('#((?:[\da-f]{3}){1,2})', re.IGNORECASE)
	rgb_re = re.compile('rgba?\(([\d, \%\.]+)\)', re.IGNORECASE)

	hex_match = hex_re.match(word)
	rgb_match = rgb_re.match(word)

	if hex_match:
		hex_color = hex_match.group(1)

		if len(hex_color) == 6:
			r,g,b = tuple(int(hex_color[i:i+2], 16) for i in range(0, 6, 2))
		else:
			r,g,b = tuple(int(hex_color[i:i+1], 16)*17 for i in range(0, 3))
		if force_alpha:
			return rgb_to_hsl(r,g,b,1)
		else:
			return rgb_to_hsl(r,g,b)



	elif rgb_match:
		rgb_list = rgb_match.group(1).split(",")
		rgb_list_len = len(rgb_list)

		if 3 <= rgb_list_len <= 4:
			r,g,b = list(map(get_decimal,rgb_list[0:3]))

			if rgb_list_len == 4:
				a = rgb_list[3].strip()
			elif force_alpha:
				a = 1
			else:
				a = None

			return rgb_to_hsl(r,g,b,a)

	# return True



def rgb_to_hsl(r,g,b,a = None):
	# From http://sebsauvage.net/python/snyppets/#hsl

	if not (0 <= r <=255): raise ValueError("r (red) parameter must be between 0 and 255.")
	if not (0 <= g <=255): raise ValueError("g (green) parameter must be between 0 and 255.")
	if not (0 <= b <=255): raise ValueError("b (blue) parameter must be between 0 and 255.")

	var_R = r/255.0
	var_G = g/255.0
	var_B = b/255.0

	var_Min = min( var_R, var_G, var_B )    # Min. value of RGB
	var_Max = max( var_R, var_G, var_B )    # Max. value of RGB
	del_Max = var_Max - var_Min             # Delta RGB value

	l = ( var_Max + var_Min ) / 2.0
	h = 0.0
	s = 0.0
	if del_Max!=0.0:
		if l<0.5: s = del_Max / ( var_Max + var_Min )
		else:     s = del_Max / ( 2.0 - var_Max - var_Min )
		del_R = ( ( ( var_Max - var_R ) / 6.0 ) + ( del_Max / 2.0 ) ) / del_Max
		del_G = ( ( ( var_Max - var_G ) / 6.0 ) + ( del_Max / 2.0 ) ) / del_Max
		del_B = ( ( ( var_Max - var_B ) / 6.0 ) + ( del_Max / 2.0 ) ) / del_Max
		if    var_R == var_Max : h = del_B - del_G
		elif  var_G == var_Max : h = ( 1.0 / 3.0 ) + del_R - del_B
		elif  var_B == var_Max : h = ( 2.0 / 3.0 ) + del_G - del_R
		while h < 0.0: h += 1.0
		while h > 1.0: h -= 1.0

	if a:
		if float(a) > 1:
			a = 1
		elif float(a) < 0:
			a = 0
		return css_hsl(h,s,l,a)
	else:
		return css_hsl(h,s,l)



def percent_str( val):
	if val > 1:
		tmp_val = val
	else:
		tmp_val = round(val * 100)

	return str(int(tmp_val)) + "%"



def css_hsl(h,s,l,a = None):
	hsl_str = str(int(round(h * 360))) + ", " + percent_str(s) + ", " + percent_str(l)
	if a:
		if (0 < float(a) < 1):
			a = round(float(a),3)
		return "hsla(" + hsl_str + ", " + str(a) + ")"
	else:
		return "hsl(" + hsl_str + ")"



def get_decimal(val):
	val_strip = val.strip()
	if isinstance(val_strip, str) and val_strip[-1] == "%":
		return round(int(val_strip[:-1]) * 255 / 100)
	else:
		return int(val_strip)


