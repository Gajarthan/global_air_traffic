# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--12_17:16:13_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-07-12 17:16:13 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-07-12 17:16:13 UTC

- **138,940** saved flights
- **46,816** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **138,940** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,668,865.8 tonnes** estimated CO2 emissions
- **96,745,841 km** total distance flown
- **854 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5670 |
| 2 | SkyWest Airlines | 5085 |
| 3 | EJA | 2723 |
| 4 | IndiGo | 2559 |
| 5 | American Airlines | 2190 |
| 6 | Southwest Airlines | 2093 |
| 7 | ENY | 1738 |
| 8 | Delta Air Lines | 1648 |
| 9 | Lufthansa | 1421 |
| 10 | LATAM Airlines | 1276 |
| 11 | Vueling | 1201 |
| 12 | WIF | 1198 |
| 13 | AZU | 1191 |
| 14 | LXJ | 1064 |
| 15 | AXM | 1041 |
| 16 | Swiss International | 990 |
| 17 | easyJet | 903 |
| 18 | All Nippon Airways | 892 |
| 19 | Alaska Airlines | 874 |
| 20 | QLK | 865 |
| 21 | EJU | 859 |
| 22 | VIV | 763 |
| 23 | AEE | 747 |
| 24 | Air France | 747 |
| 25 | CXK | 744 |
| 26 | JetBlue | 730 |
| 27 | United Airlines | 729 |
| 28 | Cathay Pacific | 728 |
| 29 | MXY | 722 |
| 30 | GLO | 712 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 119239 |
| 2 | 🇪🇸 ES | 9134 |
| 3 | 🇮🇳 IN | 8016 |
| 4 | 🇦🇺 AU | 7926 |
| 5 | 🇧🇷 BR | 7831 |
| 6 | 🇨🇦 CA | 7296 |
| 7 | 🇮🇹 IT | 7274 |
| 8 | 🇩🇪 DE | 7270 |
| 9 | 🇬🇧 GB | 6321 |
| 10 | 🇯🇵 JP | 5845 |
| 11 | 🇫🇷 FR | 5548 |
| 12 | 🇨🇴 CO | 4391 |
| 13 | 🇲🇽 MX | 4022 |
| 14 | 🇬🇷 GR | 3959 |
| 15 | 🇳🇴 NO | 3747 |
| 16 | 🇨🇭 CH | 3613 |
| 17 | 🇹🇷 TR | 3256 |
| 18 | 🇲🇾 MY | 2702 |
| 19 | 🇵🇱 PL | 2332 |
| 20 | 🇿🇦 ZA | 2284 |
| 21 | 🇳🇿 NZ | 2134 |
| 22 | 🇹🇭 TH | 2105 |
| 23 | 🇰🇷 KR | 2005 |
| 24 | 🇵🇭 PH | 1891 |
| 25 | 🇬🇹 GT | 1845 |
| 26 | 🇲🇦 MA | 1462 |
| 27 | 🇲🇪 ME | 1380 |
| 28 | 🇳🇱 NL | 1306 |
| 29 | 🇭🇷 HR | 1259 |
| 30 | 🇲🇴 MO | 1188 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2878 |
| 2 | Denver International Airport |  | US | 2323 |
| 3 | Tokyo International Airport |  | JP | 1900 |
| 4 | Indira Gandhi International Airport |  | IN | 1772 |
| 5 | Harry Reid International Airport |  | US | 1731 |
| 6 | Guaymaral Airport |  | CO | 1692 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1604 |
| 8 | Zurich Airport |  | CH | 1550 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1459 |
| 10 | La Aurora Airport |  | GT | 1425 |
| 11 | Frankfurt am Main International Airport |  | DE | 1371 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1328 |
| 13 | Chicago O'Hare International Airport |  | US | 1307 |
| 14 | El Dorado International Airport |  | CO | 1235 |
| 15 | Salt Lake City International Airport |  | US | 1232 |
| 16 | General Edward Lawrence Logan International Airport |  | US | 1190 |
| 17 | Macau International Airport |  | MO | 1188 |
| 18 | Capua Airport |  | IT | 1144 |
| 19 | Madrid Barajas International Airport |  | ES | 1131 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1119 |
| 21 | Congonhas Airport |  | BR | 1117 |
| 22 | Kuala Lumpur International Airport |  | MY | 1048 |
| 23 | Charlotte/Douglas International Airport |  | US | 1017 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 999 |
| 25 | Charles de Gaulle International Airport |  | FR | 990 |
| 26 | Bengaluru International Airport |  | IN | 960 |
| 27 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 957 |
| 28 | Malpensa International Airport |  | IT | 905 |
| 29 | Ninoy Aquino International Airport |  | PH | 880 |
| 30 | Daniel K Inouye International Airport |  | US | 853 |
| 31 | Barcelona International Airport |  | ES | 847 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 844 |
| 33 | Tenerife Norte Airport |  | ES | 814 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 813 |
| 35 | Calgary International Airport |  | CA | 802 |
| 36 | Viracopos International Airport |  | BR | 793 |
| 37 | Scottsdale Airport |  | US | 791 |
| 38 | Seattle-Tacoma International Airport |  | US | 790 |
| 39 | Amsterdam Airport Schiphol |  | NL | 782 |
| 40 | Vitoria/Foronda Airport |  | ES | 776 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 713 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 503 | 21m | 244 km | 2,118.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 341 | 24m | 225 km | 1,322.9 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 341 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 330 | 1h 9m | 770 km | 4,383.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 297 | 14m | 114 km | 582.5 t |
| 8 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 288 | 1h 7m | 706 km | 3,506.4 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 263 | 28m | 304 km | 1,378.7 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 258 | 26m | 275 km | 1,222.6 t |
| 11 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 254 | 32m | - | - |
| 12 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 206 | 22m | 55 km | 195.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 190 | 26m | 215 km | 703.7 t |
| 15 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 189 | 44m | 241 km | 785.1 t |
| 16 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 187 | 1h 46m | 1,423 km | 4,589.3 t |
| 17 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 186 | 20m | 99 km | 318.6 t |
| 18 | Bodø Airport (ENBO) | ENEN (ENEN) | 184 | 13m | - | - |
| 19 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 176 | 27m | 152 km | 460.0 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 175 | 20m | 250 km | 755.9 t |
| 21 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 172 | 30m | 49 km | 145.4 t |
| 22 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 169 | 31m | 369 km | 1,075.7 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 168 | 18m | 144 km | 417.9 t |
| 24 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 163 | 44m | 452 km | 1,270.3 t |
| 25 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 162 | 1h 16m | 961 km | 2,685.2 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 160 | 1h 1m | 695 km | 1,917.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 157 | 1h 38m | 1,156 km | 3,132.1 t |
| 28 | Glendale Regional Airport (KGEU) | Cottonwood Airport (KP52) | 156 | 54m | 136 km | 365.7 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 155 | 14m | 154 km | 410.7 t |
| 30 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 152 | 13m | - | - |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N406KT |  | Fremont County Airport (K1V6) | Mann Ranch Airport (95CO) | 2026-07-12 16:46 UTC | 2026-07-12 17:16 UTC | 30m |
| CPA501 | Cathay Pacific | Narita International Airport (RJAA) | Chek Lap Kok International Airport (VHHH) | 2026-07-12 13:34 UTC | 2026-07-12 17:13 UTC | 3h 39m |
| N586EF |  | Lancaster Airport (KLNS) | Reading Regional/Carl A Spaatz Field (KRDG) | 2026-07-12 16:57 UTC | 2026-07-12 17:12 UTC | 14m |
| N546MC |  | Jerry Sumners Sr Aurora Municipal Airport (K2H2) | Springfield-Branson Ntl Airport (KSGF) | 2026-07-12 16:58 UTC | 2026-07-12 17:10 UTC | 11m |
| N851MB |  | Boulder Municipal Airport (KBDU) | Elk Park Ranch Airport (34CD) | 2026-07-12 16:58 UTC | 2026-07-12 17:09 UTC | 10m |
| N999VP |  | IS95 (IS95) | 7IL8 (7IL8) | 2026-07-12 16:44 UTC | 2026-07-12 17:05 UTC | 21m |
| WIF732 | WIF | Trondheim Airport Vaernes (ENVA) | Sandnessjoen Airport Stokka (ENST) | 2026-07-12 16:20 UTC | 2026-07-12 17:05 UTC | 44m |
| ANE02TH | ANE | Madrid Barajas International Airport (LEMD) | Toulouse-Blagnac Airport (LFBO) | 2026-07-12 16:16 UTC | 2026-07-12 17:04 UTC | 48m |
| G20687 |  | Mcnary Field (KSLE) | Mcnary Field (KSLE) | 2026-07-12 16:39 UTC | 2026-07-12 17:04 UTC | 24m |
| PROFH | PRO | SBMM (SBMM) | SBMM (SBMM) | 2026-07-12 16:41 UTC | 2026-07-12 17:03 UTC | 21m |
| N182KQ |  | 61WA (61WA) | Boeing Field/King County International Airport (KBFI) | 2026-07-12 16:36 UTC | 2026-07-12 17:03 UTC | 26m |
| N500GP |  | Doylestown Airport (KDYL) | Doylestown Airport (KDYL) | 2026-07-12 16:36 UTC | 2026-07-12 17:01 UTC | 24m |
| N682AC |  | TE77 (TE77) | Bb Airpark (TE88) | 2026-07-12 16:23 UTC | 2026-07-12 16:59 UTC | 35m |
| GFRGP | GFR | Fairoaks Airport (EGTF) | Manchester Airport (EGCC) | 2026-07-12 16:12 UTC | 2026-07-12 16:59 UTC | 46m |
| 4XCZY |  | Haifa International Airport (LLHA) | Paphos International Airport (LCPH) | 2026-07-12 16:06 UTC | 2026-07-12 16:58 UTC | 52m |
| PRJHH | PRJ | SBMM (SBMM) | SBMM (SBMM) | 2026-07-12 16:37 UTC | 2026-07-12 16:56 UTC | 19m |
| CAP418 | CAP | Fullerton Municipal Airport (KFUL) | Big Bear City Airport (KL35) | 2026-07-12 15:51 UTC | 2026-07-12 16:56 UTC | 1h 5m |
| N445D |  | Trenton Mercer Airport (KTTN) | Doylestown Airport (KDYL) | 2026-07-12 16:12 UTC | 2026-07-12 16:55 UTC | 42m |
| N88HR |  | Visalia Municipal Airport (KVIS) | Herlong Airport (KH37) | 2026-07-12 16:11 UTC | 2026-07-12 16:55 UTC | 44m |
| N11YQ |  | Frederick Douglass/Greater Rochester International Airport (KROC) | Frederick Douglass/Greater Rochester International Airport (KROC) | 2026-07-12 16:52 UTC | 2026-07-12 16:54 UTC | 2m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
