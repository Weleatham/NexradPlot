import matplotlib

# Script to create color maps for. Needs to be hex. 
# Used google RGB to Hex converter to get colortable.
# First some radar colormaps

awips_z = [
	"#7350af", # -30 dBZ
	"#c45958", # -25 dBZ
	"#969650", # -20 dBZ
	"#b4b481", # -15 dBZ
	"#d2d2b4", # -10 dBZ
	"#91bc9f", # - 5 dBZ
	"#40a3a4", # 0 dBZ
	"#0083ae", # 5 dBZ
	"#415aa0", # 10 dBZ
	"#3ea9d6", # 15 dBZ
	"#00dcb7", # 20 dBZ
	"#0fc315", # 25 dBZ
	"#0b9316", # 30 dBZ
	"#0a5f13", # 35 dBZ
	"#fff505", # 40 dBZ
	"#ffbe00", # 45 dBZ
	"#ff0000", # 50 dBZ
	"#780000", # 55 dBZ
	"#ffffff", # 60 dBZ
	"#c9a1ff", # 65 dBZ
	"#ae00ff", # 70 dBZ
	"#05dde1", # 75 dBZ
	"#04aaac", # 80 dBZ
	"#014c4c", # 85 dBZ
	"#002323"# 90 dBZ
]

awips_z_clr = matplotlib.colors.ListedColormap(awips_z)

twip_z = [
	"#000000", # -30 dBZ
	"#040005",
	"#08000B",
	"#0C0010",
	"#100015",
	"#14001B", # -25 dBZ
	"#180020",
	"#1C0025",
	"#20002B",
	"#240030",
	"#280035", # -20 dBZ
	"#2C003B",
	"#300040",
	"#340045",
	"#38004B",
	"#3C0050", # -15 dBZ
	"#3D074F",
	"#3D0D4D",
	"#3E144C",
	"#3E1A4A",
	"#3F2149", # -10 dBZ
	"#3F2747",
	"#402E46",
	"#403444",
	"#413B43",
	"#414141", # -5 dBZ
	"#4F4F4F",
	"#5C5C5C",
	"#6A6A6A",
	"#777777",
	"#858585", # 0 dBZ
	"#929292",
	"#A0A0A0",
	"#ADADAD",
	"#BBBBBB",
	"#C8C8C8", # 5 dBZ
	"#ADB2C0",
	"#929CB7",
	"#7787AF",
	"#5C71A6",
	"#415B9E", # 10 dBZ
	"#476AA7",
	"#4D7AB1",
	"#5289BA",
	"#5899C3",
	"#5EA8CC", # 15 dBZ
	"#64B7D6",
	"#69C7DF",
	"#6FD6E8", # 18 dBZ (actually 17.5 on GR2 pal file provided)
	"#57D5B3",
	"#3FD47E", # 20 dBZ
	"#27D349",
	"#0FD214", # 22 dBZ
	"#0EC812",
	"#0DBE11",
	"#0BB40F", # 25 dBZ
	"#0AAA0D",
	"#09A00C",
	"#08960A",
	"#068C08",
	"#058207", # 30 dBZ
	"#047805",
	"#036E03",
	"#016402",
	"#005A00", # 34 dBZ
	"#408101",
	"#80A803",
	"#BFCE04",
	"#FFF505", # 38 dBZ
	"#FEEB05",
	"#FDE104", # 40 dBZ
	"#FCD704",
	"#FBCD03",
	"#FAC303",
	"#FAB902",
	"#F9AF02", # 45 dBZ
	"#F8A501",
	"#F79B01",
	"#F69100",
	"#F58700", # 49 dBZ
	"#FF0000", # 50 dBZ
	"#FF121A",
	"#FF2333",
	"#FF354D",
	"#FF4766",
	"#FF5980", # 55 dBZ
	"#FF6A99",
	"#FF7CB3",
	"#FF8ECC",
	"#FF9FE6",
	"#FFB1FF", # 60 dBZ
	"#FFC1FF",
	"#FFD0FF",
	"#FFE0FF",
	"#FFEFFF",
	"#FFFFFF", # 65 dBZ
	"#E6E6FF",
	"#CCCCFF",
	"#B3B3FF",
	"#9999FF",
	"#8080FF", # 70 dBZ
	"#6666FF",
	"#4C4CFF",
	"#3333FF",
	"#1A1AFF",
	"#0000FF", # 75 dBZ
	"#0000FF",
	"#0000FF",
	"#0000FF",
	"#0000FF",
	"#0000FF" # 80 dBZ
]

twip_z_clr = matplotlib.colors.ListedColormap(twip_z)

miller_z = [
	"#000000", # -30 dBZ
	"#3c0050", # -10 dBZ
	"#505050", # 5 dBZ
	"#919191", # 10 dBZ
	"#b9b9b9", # 18 dBZ
	"#00ff00", # 22 dBZ
	"#005a00", # 34 dBZ
	"#ffff00", # 38 dBZ
	"#ffbf00", # 42 dBZ
	"#f07800", # 48 dBZ
	"#ff0000", # 51 dBZ
	"#5a0000", # 60 dBZ
	"#280000", # 65 dBZ
	"#bebebe", # 70 dBZ
	"#ffffff", # 72 dBZ
	"#ffff00" # 80 dBZ
]

miller_z_clr = matplotlib.colors.ListedColormap(miller_z)

enhance_bv = [
	"#ffffff", # -120 kts
	"#ffffff",
	"#ffffff",
	"#ffffff",
	"#ffffff",
	"#ffffff", # -115 kts
	"#ffffff",
	"#ffffff",
	"#ffffff",
	"#ffffff",
	"#ffffff", # -110 kts
	"#ffffff",
	"#ffffff",
	"#ffffff",
	"#ffffff",
	"#ffffff", # -105 kts
	"#ffffff",
	"#ffffff",
	"#ffffff",
	"#ffffff",
	"#ffffff", # -100 kts
	"#ffffff",
	"#ffffff",
	"#ffffff",
	"#ffffff",
	"#ffffff", # -95 kts
	"#ffffff",
	"#ffffff",
	"#ffffff",
	"#ffffff",
	"#ffffff", # -90 kts
	"#ffffff",
	"#ffffff",
	"#ffffff",
	"#ffffff",
	"#ffffff", # -85 kts
	"#FBDBF6",
	"#F8B6EC",
	"#F492E3",
	"#F16DDA",
	"#ED49D1", # -80 kts
	"#EA24C7",
	"#E600BE", # -78 kts
	"#C900B3",
	"#AD00A8",
	"#90009C", # -75 kts
	"#730091",
	"#560086",
	"#3A007B",
	"#1D006F",
	"#000064", # -70 kts
	"#050D6C",
	"#0A1A74",
	"#0F267B",
	"#143383",
	"#19408B", # -65 kts
	"#1E4D93",
	"#23599A",
	"#2866A2",
	"#2D73AA",
	"#3280B2", # -60 kts
	"#378CB9",
	"#3C99C1",
	"#41A6C9",
	"#46B3D1",
	"#4BBFD8", # -55 kts
	"#50CCE0",
	"#55D9E8",
	"#5AE6F0",
	"#5FF2F7",
	"#64FFFF", # -50 kts
	"#96FF96", # -49 kts
	"#8BFF8B",
	"#81FF81",
	"#76FF76",
	"#6BFF6B", # -45 kts
	"#60FF60",
	"#56FF56",
	"#4BFF4B",
	"#40FF40",
	"#36FF36", # -40 kts
	"#2BFF2B",
	"#20FF20",
	"#15FF15",
	"#0BFF0B",
	"#00FF00", # -35 kts
	"#00F600",
	"#00ED00",
	"#00E300",
	"#00DA00",
	"#00D100", # -30 kts
	"#00C800",
	"#00BE00",
	"#00B500",
	"#00AC00",
	"#00A300", # -25 kts
	"#009900",
	"#009000",
	"#008700",
	"#007D00",
	"#007400", # -20 kts
	"#006B00",
	"#006200",
	"#005900",
	"#004F00",
	"#004600", # -15 kts
	"#0C4D0C",
	"#185518",
	"#245C24",
	"#306330",
	"#3C6B3C", # -10 kts
	"#487248",
	"#547954",
	"#608160",
	"#6C886C",
	"#788F78", # -5 kts
	"#849784",
	"#909E90",
	"#9CA59C",
	"#A8ADA8",
	"#B4B4B4", # 0 kts
	"#ADA8A8",
	"#A59C9C",
	"#9E9090",
	"#978484",
	"#8F7878", # 5 kts 
	"#886C6C",
	"#816060",
	"#795454",
	"#724848",
	"#6B3C3C", # 10 kts
	"#633030",
	"#5C2424",
	"#551818",
	"#4D0C0C",
	"#460000", # 15 kts
	"#4F0000",
	"#590000",
	"#620000",
	"#6B0000",
	"#740000", # 20 kts 
	"#7E0000",
	"#870000",
	"#900000",
	"#990000",
	"#A30000", # 25 kts 
	"#AC0000",
	"#B50000",
	"#BE0000",
	"#C80000",
	"#D10000", # 30 kts 
	"#DA0000",
	"#E30000",
	"#ED0000",
	"#F60000",
	"#FF0000", # 35 kts
	"#FF0D0D",
	"#FF1A19",
	"#FF2726",
	"#FF3332",
	"#FF403E", # 40 kts
	"#FF4D4B",
	"#FF5A58",
	"#FF6764",
	"#FF7470",
	"#FF817D", # 45 kts
	"#FF8D8A",
	"#FF9A96",
	"#FFA7A3",
	"#FFB4AF", # 49 kts
	"#FF8C46", # 50 kts
	"#FD8A43",
	"#FA883F",
	"#F8863C",
	"#F58438",
	"#F38235", # 55 kts 
	"#F08031",
	"#EE7E2E",
	"#EB7C2A",
	"#E97A27",
	"#E67823", # 60 kts
	"#E4761F",
	"#E1741C",
	"#DF7219",
	"#DC7015",
	"#DA6E12", # 65 kts
	"#D76C0E",
	"#D56A0A",
	"#D26807",
	"#D06603",
	"#CD6400", # 70 kts
	"#D37700",
	"#DA8B00",
	"#E09E00",
	"#E6B200",
	"#ECC500", # 75 kts
	"#F3D800",
	"#F9EC00",
	"#FFFF00", # 78 kts
	"#E2E207",
	"#C4C40E", # 80 kts
	"#A7A715",
	"#8A8A1D",
	"#6D6D24",
	"#4F4F2B",
	"#323232", # 85 kts
	"#323232",
	"#323232",
	"#323232",
	"#323232",
	"#323232", # 90 kts
	"#323232",
	"#323232",
	"#323232",
	"#323232",
	"#323232", # 95 kts
	"#323232",
	"#323232",
	"#323232",
	"#323232",
	"#323232", # 100 kts
	"#323232",
	"#323232",
	"#323232",
	"#323232",
	"#323232", # 105 kts
	"#323232",
	"#323232",
	"#323232",
	"#323232",
	"#323232", # 110 kts
	"#323232",
	"#323232",
	"#323232",
	"#323232",
	"#323232", # 115 kts
	"#323232",
	"#323232",
	"#323232",
	"#323232",
	"#323232" # 120 kts
]

enhanced_bv_clr = matplotlib.colors.ListedColormap(enhance_bv)

awips_cc = [
	"#140032", # 0.20
    "#140033", 
    "#150034", 
    "#150036",
    "#160037",
    "#160038", # 0.25
    "#160039",
    "#17003A",
    "#17003C",
    "#18003D",
    "#18003E", # 0.30
    "#18003F",
    "#190040",
    "#190042",
    "#1A0043",
    "#1A0044", # 0.35
    "#1A0045",
    "#1B0046",
    "#1B0048",
    "#1C0049",
    "#1C004A", # 0.40
    "#1C004B",
    "#1D004C",
    "#1D004E",
    "#1E004F",
    "#1E0050", # 0.45
    "#1B0053",
    "#180056",
    "#150059",
    "#12005C",
    "#0F005F", # 0.50
    "#0C0062",
    "#090065",
    "#060068",
    "#03006B",
    "#00006E", # 0.55
    "#000072",
    "#000076",
    "#00007A",
    "#00007E",
    "#000082", # 0.60
    "#000086",
    "#00008A",
    "#00008E",
    "#000092",
    "#000096", # 0.65
    "#00009A",
    "#00009E",
    "#0000A2",
    "#0000A6",
    "#0000AA", # 0.70
    "#0000BB",
    "#0000CC",
    "#0000DD",
    "#0000EE",
    "#0000FF", # 0.75
    "#1919FF",
    "#3232FF",
    "#4B4BFF",
    "#6464FF",
    "#7D7DFF", # 0.80
    "#7597DD",
    "#6DB1BB",
    "#65CB99",
    "#5DE577",
    "#55FF55", # 0.85
    "#60F940",
    "#6CF32B",
    "#77EC15",
    "#82E600", # 0.89
    "#FFFF00", # 0.90
    "#FFD200", # 0.91 (is 0.915 on GR)
    "#FFB100",
    "#FF8F00",
    "#FF6E00", # 0.94
    "#FF3700", # 0.95
    "#FF0000", # 0.96
    "#A80000", 
    "#500000", # 0.98
    "#710044",
    "#910087", # 1.00
    "#FFA5FF", # 1.01 (is 1.001 on GR)
    "#FFA5FF",
    "#FFA5FF",
    "#FFA5FF" # 1.04
]

awips_cc_clr = matplotlib.colors.ListedColormap(awips_cc)

awips_zdr = [
	"#000000", # -4 db
	"#0e0e0e", # -3.75 db
	"#1c1c1c", # -3.5 db
	"#292929", # -3.25 db
	"#373737", # -3 db
	"#454545", # -2.75 db
	"#535353", # -2.5 db
	"#606060", # -2.25 db
	"#6e6e6e", # -2 db
	"#7c7c7c", # -1.75 db
	"#8a8a8a", # -1.5 db
	"#979797", # -1.25 db
	"#a5a5a5", # -1 db
	"#9f9aa9", # -0.75 db
	"#9a8fad", # -0.50 db
	"#9484b1", # -0.25 db
	"#8e79b5", # 0 db (#dcdcdc other option)
	"#0a0a9b", # 0.25 db
	"#1d59ae", # 0.50 db
	"#31a9c1", # 0.75 db
	"#44f8d4", # 1 db
	"#4feb9b", # 1.25 db
	"#5add62", # 1.5 db
	"#adee63", # 1.75 db
	"#ffff64", # 2 db
	"#f6c24c", # 2.25 db
	"#ee8535", # 2.5 db
	"#e5471d", # 2.75 db
	"#dc0a05", # 3 db
	"#d10804", # 3.25 db
	"#c60503", # 3.5 db
	"#ba0301", # 3.75 db
	"#af0000", # 4 db
	"#bf1e2d", # 4.25 db
	"#d03c5a", # 4.5 db
	"#e05a87", # 4.75 db
	"#f078b4", # 5 db
	"#f49ac7", # 5.25 db
	"#f8bcda", # 5.5 db
	"#fbddec", # 5.75 db
	"#ffffff", # 6 db
	"#f1e5f2", # 6.25 db
	"#e4cbe5", # 6.5 db
	"#d6b0d8", # 6.75 db
	"#c896cb", # 7 db
	"#ba7cbd", # 7.25 db
	"#ad62b0", # 7.5 db
	"#9f47a3", # 7.75 db
	"#912d96", # 8 db
]

awips_zdr_clr = matplotlib.colors.ListedColormap(awips_zdr)

awips_kdp = [
	"#8E8E8E", # -3 deg/km
	"#898989",
	"#838383",
	"#7E7E7E",
	"#787878", # -2 deg/km
	"#737373",
	"#6F6F6F",
	"#6A6A6A",
	"#656565", # -1 deg/km
	"#565656", 
	"#464646", # -0.5 deg/km
	"#76283c", 
	"#a60a32", # 0 deg/km
	"#B92244", # 0.25 deg/km
	"#CC3956", # 0.5 deg/km
	"#D8517C",
	"#E469A1", # 1.0 deg/km
	"#C573AD",
	"#A67DB9", # 1.5 deg/km
	"#80BEDC",
	"#5AFFFF", # 2.0 deg/km
	"#43DBAE",
	"#2BB75D", # 2.5 deg/km
	"#20D739",
	"#14F614", # 3.0 deg/km 
	"#4FF710",
	"#8AF90C",
	"#C4FA07",
	"#FFFB03", # 4.0 deg/km
	"#FFDD08",
	"#FFBE0C",
	"#FFA011",
	"#FF8115", # 5.0 deg/km
	"#FF8922",
	"#FF9130",
	"#FF993D",
	"#FFA24B", # 6.0 deg/km
	"#FFAA58",
	"#FFB265",
	"#FFBA73",
	"#FFC280", # 7.0 deg/km
	"#E49B7F",
	"#C8747F",
	"#AD4C7E",
	"#91257D", # 8.0 deg/km
]

awips_kdp_clr = matplotlib.colors.ListedColormap(awips_kdp)

miller_sw = [
	"#2D2D2D", # 0 kts
	"#323232",
	"#373737", # 2 kts
	"#414141",
	"#4B4B4B", # 4 kts
	"#757575",
	"#9E9E9E",
	"#C8C8C8", # 7 kts
	"#E4D764",
	"#FFE600", # 9 kts
	"#FFC300",
	"#FFA000", # 11 kts
	"#FF6E00",
	"#FF3C00",
	"#FF0A00", # 14 kts
	"#FF0821",
	"#FF0743",
	"#FF0564",
	"#FF0385",
	"#FF02A7",
	"#FF00C8", # 20 kts
	"#FF20CF",
	"#FF40D6",
	"#FF60DD",
	"#FF80E4",
	"#FF9FEA",
	"#FFBFF1",
	"#FFDFF8",
	"#FFFFFF", # 28 kts
	"#ECFFFF",
	"#D9FFFF",
	"#C6FFFF",
	"#B2FFFF",
	"#9FFFFF",
	"#8CFFFF", # 34 kts
	"#82FCFC",
	"#78F8F8",
	"#6EF5F5",
	"#64F2F2",
	"#5AEEEE",
	"#50EBEB", # 40 kts
]

miller_sw_clr = matplotlib.colors.ListedColormap(miller_sw)
