# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--28_10:46:04_UTC-green)

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

**Latest saved flight:** 2026-06-28 10:46:04 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-28 10:46:04 UTC

- **122,349** saved flights
- **41,984** unique routes
- **134** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **122,349** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **1,479,831.2 tonnes** estimated CO2 emissions
- **85,787,314 km** total distance flown
- **858 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 5014 |
| 2 | SkyWest Airlines | 4518 |
| 3 | EJA | 2367 |
| 4 | IndiGo | 2342 |
| 5 | American Airlines | 1890 |
| 6 | Southwest Airlines | 1834 |
| 7 | ENY | 1528 |
| 8 | Delta Air Lines | 1449 |
| 9 | Lufthansa | 1323 |
| 10 | LATAM Airlines | 1092 |
| 11 | Vueling | 1091 |
| 12 | WIF | 1079 |
| 13 | AZU | 1025 |
| 14 | AXM | 988 |
| 15 | LXJ | 932 |
| 16 | Swiss International | 855 |
| 17 | All Nippon Airways | 832 |
| 18 | Alaska Airlines | 803 |
| 19 | easyJet | 786 |
| 20 | QLK | 778 |
| 21 | EJU | 766 |
| 22 | Cathay Pacific | 687 |
| 23 | AEE | 678 |
| 24 | Air France | 669 |
| 25 | VIV | 665 |
| 26 | United Airlines | 659 |
| 27 | CXK | 649 |
| 28 | MXY | 638 |
| 29 | JetBlue | 611 |
| 30 | AXB | 608 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 103883 |
| 2 | 🇪🇸 ES | 8258 |
| 3 | 🇮🇳 IN | 7359 |
| 4 | 🇦🇺 AU | 7177 |
| 5 | 🇧🇷 BR | 6755 |
| 6 | 🇩🇪 DE | 6508 |
| 7 | 🇮🇹 IT | 6506 |
| 8 | 🇨🇦 CA | 6436 |
| 9 | 🇯🇵 JP | 5427 |
| 10 | 🇬🇧 GB | 5385 |
| 11 | 🇫🇷 FR | 4858 |
| 12 | 🇨🇴 CO | 4027 |
| 13 | 🇲🇽 MX | 3562 |
| 14 | 🇬🇷 GR | 3492 |
| 15 | 🇳🇴 NO | 3364 |
| 16 | 🇨🇭 CH | 3139 |
| 17 | 🇲🇾 MY | 2556 |
| 18 | 🇹🇷 TR | 2543 |
| 19 | 🇿🇦 ZA | 2035 |
| 20 | 🇵🇱 PL | 2011 |
| 21 | 🇳🇿 NZ | 1986 |
| 22 | 🇹🇭 TH | 1931 |
| 23 | 🇰🇷 KR | 1926 |
| 24 | 🇵🇭 PH | 1756 |
| 25 | 🇬🇹 GT | 1699 |
| 26 | 🇲🇦 MA | 1312 |
| 27 | 🇲🇪 ME | 1219 |
| 28 | 🇲🇴 MO | 1176 |
| 29 | 🇳🇱 NL | 1168 |
| 30 | 🇭🇷 HR | 1055 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2568 |
| 2 | Denver International Airport |  | US | 2056 |
| 3 | Tokyo International Airport |  | JP | 1797 |
| 4 | Indira Gandhi International Airport |  | IN | 1621 |
| 5 | Harry Reid International Airport |  | US | 1527 |
| 6 | Guaymaral Airport |  | CO | 1517 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1477 |
| 8 | Zurich Airport |  | CH | 1355 |
| 9 | La Aurora Airport |  | GT | 1312 |
| 10 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1301 |
| 11 | Frankfurt am Main International Airport |  | DE | 1277 |
| 12 | Phoenix Sky Harbor International Airport |  | US | 1203 |
| 13 | Chicago O'Hare International Airport |  | US | 1186 |
| 14 | Macau International Airport |  | MO | 1176 |
| 15 | El Dorado International Airport |  | CO | 1171 |
| 16 | Salt Lake City International Airport |  | US | 1062 |
| 17 | Capua Airport |  | IT | 1044 |
| 18 | Madrid Barajas International Airport |  | ES | 1021 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1019 |
| 20 | Kuala Lumpur International Airport |  | MY | 993 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 963 |
| 22 | Congonhas Airport |  | BR | 948 |
| 23 | Charlotte/Douglas International Airport |  | US | 923 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 905 |
| 25 | Charles de Gaulle International Airport |  | FR | 896 |
| 26 | Bengaluru International Airport |  | IN | 883 |
| 27 | Malpensa International Airport |  | IT | 850 |
| 28 | Ninoy Aquino International Airport |  | PH | 814 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 798 |
| 30 | Daniel K Inouye International Airport |  | US | 785 |
| 31 | Barcelona International Airport |  | ES | 768 |
| 32 | Tenerife Norte Airport |  | ES | 763 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 748 |
| 34 | Calgary International Airport |  | CA | 717 |
| 35 | Vitoria/Foronda Airport |  | ES | 711 |
| 36 | Norman Y Mineta San Jose International Airport |  | US | 706 |
| 37 | Amsterdam Airport Schiphol |  | NL | 706 |
| 38 | Scottsdale Airport |  | US | 704 |
| 39 | Seattle-Tacoma International Airport |  | US | 702 |
| 40 | Don Mueang International Airport |  | TH | 698 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 632 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 445 | 21m | 244 km | 1,873.8 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 320 | 24m | 225 km | 1,241.4 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 310 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 296 | 1h 10m | 770 km | 3,932.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 294 | 1h 25m | 910 km | 4,613.5 t |
| 7 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 287 | 1h 7m | 706 km | 3,494.2 t |
| 8 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 262 | 28m | 304 km | 1,373.5 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 240 | 26m | 275 km | 1,137.3 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 235 | 19m | 165 km | 668.5 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 231 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 178 | 22m | 55 km | 169.2 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 177 | 26m | 215 km | 655.5 t |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 174 | 20m | 99 km | 298.0 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 170 | 13m | - | - |
| 17 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 166 | 44m | 241 km | 689.5 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 166 | 27m | 152 km | 433.8 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 158 | 31m | 369 km | 1,005.7 t |
| 20 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 156 | 1h 44m | 1,423 km | 3,828.5 t |
| 21 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 155 | 44m | 452 km | 1,208.0 t |
| 22 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 154 | 18m | 144 km | 383.1 t |
| 24 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 151 | 20m | 250 km | 652.2 t |
| 25 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 142 | 1h 38m | 1,156 km | 2,832.8 t |
| 26 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 141 | 1h 1m | 695 km | 1,690.2 t |
| 27 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 139 | 1h 17m | 961 km | 2,304.0 t |
| 28 | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 137 | 29m | 49 km | 115.8 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 137 | 13m | - | - |
| 30 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 135 | 20m | 147 km | 341.6 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| AEE7RN | AEE | Eleftherios Venizelos International Airport (LGAV) | Stockholm-Arlanda Airport (ESSA) | 2026-06-28 07:28 UTC | 2026-06-28 10:46 UTC | 3h 17m |
| DEFEJ | DEF | Speyer Airport (EDRY) | Frankfurt-Egelsbach Airport (EDFE) | 2026-06-28 10:20 UTC | 2026-06-28 10:44 UTC | 24m |
| UAE9860 | Emirates | Al Maktoum International Airport (OMDW) | Zhuhai Airport (ZGSD) | 2026-06-28 03:29 UTC | 2026-06-28 10:44 UTC | 7h 14m |
| OEFDN | OEF | Fano Airport (LIDF) | Fano Airport (LIDF) | 2026-06-28 09:05 UTC | 2026-06-28 10:39 UTC | 1h 33m |
| UBG316 | UBG | Kuala Lumpur International Airport (WMKK) | Naypyidaw Airport (VYEL) | 2026-06-28 08:20 UTC | 2026-06-28 10:33 UTC | 2h 12m |
| ZAM16 | ZAM | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-06-28 09:55 UTC | 2026-06-28 10:31 UTC | 35m |
| LOG85CB | LOG | Isle of Man Airport (EGNS) | Birmingham International Airport (EGBB) | 2026-06-28 09:45 UTC | 2026-06-28 10:28 UTC | 43m |
| BBC585 | BBC | Changi Air Base (WSAC) | Naypyidaw Airport (VYEL) | 2026-06-28 08:06 UTC | 2026-06-28 10:27 UTC | 2h 21m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-06-28 10:16 UTC | 2026-06-28 10:25 UTC | 9m |
| LHX3VJ | LHX | Munich International Airport (EDDM) | Hannover Airport (EDDV) | 2026-06-28 09:32 UTC | 2026-06-28 10:20 UTC | 48m |
|  |  | Jomo Kenyatta International Airport (HKJK) | Jomo Kenyatta International Airport (HKJK) | 2026-06-28 10:20 UTC | 2026-06-28 10:20 UTC | 0m |
| RUK1711 | RUK | Manchester Airport (EGCC) | Kenitra Airport (GMMY) | 2026-06-28 07:31 UTC | 2026-06-28 10:19 UTC | 2h 48m |
| GMA01 | GMA | Glasgow International Airport (EGPF) | Birmingham International Airport (EGBB) | 2026-06-28 09:04 UTC | 2026-06-28 10:18 UTC | 1h 14m |
| PAV328 | PAV | Hamburg Airport (EDDH) | Nuremberg Airport (EDDN) | 2026-06-28 09:21 UTC | 2026-06-28 10:14 UTC | 53m |
| BBC437 | BBC | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 2026-06-28 09:43 UTC | 2026-06-28 10:13 UTC | 29m |
| DFELI | DFE | Thalmassing-Waizenhofen Airport (EDPW) | Thalmassing-Waizenhofen Airport (EDPW) | 2026-06-28 09:01 UTC | 2026-06-28 10:13 UTC | 1h 11m |
| ANA373 | All Nippon Airways | Matsumoto Airport (RJAF) | Saga Airport (RJFS) | 2026-06-28 09:13 UTC | 2026-06-28 10:11 UTC | 57m |
| JES3100 | JES | Jorge Newbery Airpark (SABE) | Ingeniero Ambrosio Taravella Airport (SACO) | 2026-06-28 09:00 UTC | 2026-06-28 10:10 UTC | 1h 10m |
| SJV950 | SJV | Hang Nadim Airport (WIDD) | Adi Sutjipto International Airport (WARJ) | 2026-06-28 08:30 UTC | 2026-06-28 10:08 UTC | 1h 37m |
| ZAM39 | ZAM | Al Udeid Air Base (OTBH) | Al Udeid Air Base (OTBH) | 2026-06-28 09:24 UTC | 2026-06-28 10:07 UTC | 42m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
