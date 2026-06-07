# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_23:07:23_UTC-green)

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

**Latest saved flight:** 2026-06-07 23:07:23 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-07 23:07:23 UTC

- **105,680** saved flights
- **37,189** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **105,680** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,293,371.9 tonnes** estimated CO2 emissions
- **74,978,081 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4354 |
| 2 | SkyWest Airlines | 3979 |
| 3 | IndiGo | 2098 |
| 4 | EJA | 2023 |
| 5 | American Airlines | 1694 |
| 6 | Southwest Airlines | 1595 |
| 7 | ENY | 1327 |
| 8 | Delta Air Lines | 1255 |
| 9 | Lufthansa | 1211 |
| 10 | Vueling | 971 |
| 11 | LATAM Airlines | 934 |
| 12 | WIF | 926 |
| 13 | AXM | 908 |
| 14 | AZU | 852 |
| 15 | LXJ | 798 |
| 16 | Swiss International | 765 |
| 17 | All Nippon Airways | 737 |
| 18 | Alaska Airlines | 732 |
| 19 | QLK | 709 |
| 20 | easyJet | 686 |
| 21 | EJU | 670 |
| 22 | Cathay Pacific | 633 |
| 23 | AEE | 609 |
| 24 | VIV | 605 |
| 25 | Air France | 603 |
| 26 | United Airlines | 586 |
| 27 | MXY | 578 |
| 28 | CXK | 557 |
| 29 | Japan Airlines | 525 |
| 30 | AXB | 515 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 88906 |
| 2 | 🇪🇸 ES | 7270 |
| 3 | 🇮🇳 IN | 6618 |
| 4 | 🇦🇺 AU | 6361 |
| 5 | 🇧🇷 BR | 5778 |
| 6 | 🇩🇪 DE | 5677 |
| 7 | 🇮🇹 IT | 5643 |
| 8 | 🇨🇦 CA | 5504 |
| 9 | 🇯🇵 JP | 4851 |
| 10 | 🇬🇧 GB | 4462 |
| 11 | 🇫🇷 FR | 4196 |
| 12 | 🇨🇴 CO | 3645 |
| 13 | 🇲🇽 MX | 3161 |
| 14 | 🇬🇷 GR | 3004 |
| 15 | 🇳🇴 NO | 2928 |
| 16 | 🇨🇭 CH | 2702 |
| 17 | 🇲🇾 MY | 2328 |
| 18 | 🇹🇷 TR | 2036 |
| 19 | 🇿🇦 ZA | 1818 |
| 20 | 🇳🇿 NZ | 1764 |
| 21 | 🇰🇷 KR | 1756 |
| 22 | 🇹🇭 TH | 1751 |
| 23 | 🇵🇱 PL | 1720 |
| 24 | 🇵🇭 PH | 1557 |
| 25 | 🇬🇹 GT | 1529 |
| 26 | 🇲🇦 MA | 1169 |
| 27 | 🇲🇴 MO | 1106 |
| 28 | 🇳🇱 NL | 1036 |
| 29 | 🇲🇪 ME | 1011 |
| 30 | 🇭🇷 HR | 922 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2295 |
| 2 | Denver International Airport |  | US | 1809 |
| 3 | Tokyo International Airport |  | JP | 1606 |
| 4 | Indira Gandhi International Airport |  | IN | 1439 |
| 5 | Harry Reid International Airport |  | US | 1353 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1334 |
| 7 | Guaymaral Airport |  | CO | 1327 |
| 8 | Frankfurt am Main International Airport |  | DE | 1202 |
| 9 | Zurich Airport |  | CH | 1196 |
| 10 | La Aurora Airport |  | GT | 1177 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1140 |
| 12 | El Dorado International Airport |  | CO | 1112 |
| 13 | Macau International Airport |  | MO | 1106 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1066 |
| 15 | Chicago O'Hare International Airport |  | US | 1063 |
| 16 | Madrid Barajas International Airport |  | ES | 924 |
| 17 | Kuala Lumpur International Airport |  | MY | 913 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 905 |
| 19 | Salt Lake City International Airport |  | US | 903 |
| 20 | Capua Airport |  | IT | 893 |
| 21 | Charlotte/Douglas International Airport |  | US | 821 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 811 |
| 23 | Charles de Gaulle International Airport |  | FR | 802 |
| 24 | Congonhas Airport |  | BR | 801 |
| 25 | Bengaluru International Airport |  | IN | 792 |
| 26 | Malpensa International Airport |  | IT | 790 |
| 27 | Daniel K Inouye International Airport |  | US | 721 |
| 28 | Tenerife Norte Airport |  | ES | 716 |
| 29 | Ninoy Aquino International Airport |  | PH | 713 |
| 30 | Barcelona International Airport |  | ES | 692 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 683 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 682 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 679 |
| 34 | Amsterdam Airport Schiphol |  | NL | 642 |
| 35 | Don Mueang International Airport |  | TH | 641 |
| 36 | Vitoria/Foronda Airport |  | ES | 632 |
| 37 | Calgary International Airport |  | CA | 625 |
| 38 | Seattle-Tacoma International Airport |  | US | 616 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 606 |
| 40 | Netaji Subhash Chandra Bose International Airport |  | IN | 605 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 548 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 389 | 21m | 244 km | 1,638.0 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 282 | 24m | 225 km | 1,094.0 t |
| 4 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 281 | 1h 7m | 706 km | 3,421.2 t |
| 5 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 276 | 9m | - | - |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 267 | 14m | 114 km | 523.7 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 259 | 28m | 304 km | 1,357.7 t |
| 8 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 259 | 1h 25m | 910 km | 4,064.3 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 243 | 1h 10m | 770 km | 3,228.1 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 220 | 19m | 165 km | 625.8 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 210 | 26m | 275 km | 995.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 204 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 161 | 20m | 99 km | 275.8 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 155 | 27m | 215 km | 574.1 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 150 | 14m | 154 km | 397.4 t |
| 17 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 146 | 31m | 369 km | 929.3 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 146 | 27m | 152 km | 381.6 t |
| 19 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 144 | 44m | 452 km | 1,122.3 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 142 | 13m | - | - |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 139 | 18m | 144 km | 345.8 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 130 | 1h 39m | 1,156 km | 2,593.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 130 | 1h 1m | 695 km | 1,558.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 122 | 1h 43m | 1,423 km | 2,994.1 t |
| 27 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 122 | 44m | 241 km | 506.8 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 122 | 12m | - | - |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 121 | 1h 52m | 1,304 km | 2,722.2 t |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 119 | 1h 18m | 961 km | 1,972.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N8439T |  | Ramona Airport (KRNM) | Riverside Airport (KRAL) | 2026-06-07 22:25 UTC | 2026-06-07 23:07 UTC | 41m |
| N5726B |  | Mariposa-Yosemite Airport (KMPI) | Mariposa-Yosemite Airport (KMPI) | 2026-06-07 22:26 UTC | 2026-06-07 22:55 UTC | 28m |
| CPA252 | Cathay Pacific | London Heathrow Airport (EGLL) | Zhuhai Airport (ZGSD) | 2026-06-07 11:27 UTC | 2026-06-07 22:49 UTC | 11h 22m |
| CPA288 | Cathay Pacific | Frankfurt am Main International Airport (EDDF) | Zhuhai Airport (ZGSD) | 2026-06-07 12:04 UTC | 2026-06-07 22:46 UTC | 10h 41m |
| TKR873 | TKR | Bolinder Field/Tooele Valley Airport (KTVY) | UT99 (UT99) | 2026-06-07 22:30 UTC | 2026-06-07 22:45 UTC | 14m |
| N855NF |  | Bolinder Field/Tooele Valley Airport (KTVY) | UT99 (UT99) | 2026-06-07 22:31 UTC | 2026-06-07 22:44 UTC | 13m |
| UPS5744 | UPS | Chicago/Rockford International Airport (KRFD) | Dallas-Fort Worth International Airport (KDFW) | 2026-06-07 20:39 UTC | 2026-06-07 22:42 UTC | 2h 2m |
| N682AC |  | Salaika Aviation Airport (07TA) | Bb Airpark (TE88) | 2026-06-07 22:28 UTC | 2026-06-07 22:39 UTC | 11m |
| N234WL |  | Westmoreland Airport (49NY) | Laguardia Airport (KLGA) | 2026-06-07 21:58 UTC | 2026-06-07 22:36 UTC | 38m |
| LXJ393 | LXJ | Baltimore/Washington International Thurgood Marshall Airport (KBWI) | Tweed/New Haven Airport (KHVN) | 2026-06-07 21:39 UTC | 2026-06-07 22:34 UTC | 54m |
| N260SM |  | Dallas Love Field (KDAL) | Mc Elroy Airfield (K20V) | 2026-06-07 20:57 UTC | 2026-06-07 22:33 UTC | 1h 35m |
| CGSSC | CGS | Vancouver International Airport (CYVR) | Victoria International Airport (CYYJ) | 2026-06-07 21:58 UTC | 2026-06-07 22:29 UTC | 30m |
| N906MR |  | Soldotna Airport (PASX) | Big Creek Airport (AK51) | 2026-06-07 22:01 UTC | 2026-06-07 22:27 UTC | 25m |
| N951LB |  | San Gabriel Valley Airport (KEMT) | San Gabriel Valley Airport (KEMT) | 2026-06-07 22:21 UTC | 2026-06-07 22:27 UTC | 5m |
| MXY207 | MXY | Harry Reid International Airport (KLAS) | Akron-Canton Regional Airport (KCAK) | 2026-06-07 18:41 UTC | 2026-06-07 22:26 UTC | 3h 45m |
| N532LW |  | Mc Clellan-Palomar Airport (KCRQ) | Los Alamos Airport (KLAM) | 2026-06-07 20:53 UTC | 2026-06-07 22:26 UTC | 1h 32m |
| CPA372 | Cathay Pacific | Madrid Barajas International Airport (LEMD) | Zhuhai Airport (ZGSD) | 2026-06-07 10:49 UTC | 2026-06-07 22:22 UTC | 11h 33m |
| LXJ379 | LXJ | Millington/Memphis Airport (KNQA) | C A Moore Airport (K19M) | 2026-06-07 21:57 UTC | 2026-06-07 22:21 UTC | 24m |
| ENY4230 | ENY | Dallas-Fort Worth International Airport (KDFW) | Pops Landing Airport (1TN2) | 2026-06-07 20:39 UTC | 2026-06-07 22:20 UTC | 1h 40m |
| N150LE |  | Bend Municipal Airport (KBDN) | Bend Municipal Airport (KBDN) | 2026-06-07 22:13 UTC | 2026-06-07 22:20 UTC | 6m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
