# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--04_08:30:01_UTC-green)

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

**Latest saved flight:** 2026-10-04 08:30:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-10-04 08:30:01 UTC

- **275,962** saved flights
- **80,320** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **275,962** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,340,639.7 tonnes** estimated CO2 emissions
- **193,660,275 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10819 |
| 2 | SkyWest Airlines | 9604 |
| 3 | EJA | 5405 |
| 4 | IndiGo | 4600 |
| 5 | American Airlines | 4270 |
| 6 | Southwest Airlines | 4054 |
| 7 | Delta Air Lines | 3427 |
| 8 | ENY | 3225 |
| 9 | LATAM Airlines | 2672 |
| 10 | AZU | 2594 |
| 11 | Vueling | 2286 |
| 12 | WIF | 2242 |
| 13 | LXJ | 2182 |
| 14 | Lufthansa | 2074 |
| 15 | easyJet | 1833 |
| 16 | Swiss International | 1805 |
| 17 | QLK | 1778 |
| 18 | EJU | 1716 |
| 19 | AXM | 1693 |
| 20 | United Airlines | 1682 |
| 21 | Alaska Airlines | 1629 |
| 22 | All Nippon Airways | 1577 |
| 23 | PGT | 1552 |
| 24 | GLO | 1540 |
| 25 | WMT | 1535 |
| 26 | Air France | 1515 |
| 27 | VIV | 1512 |
| 28 | Wizz Air | 1489 |
| 29 | CXK | 1362 |
| 30 | AEE | 1312 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 230266 |
| 2 | 🇪🇸 ES | 17252 |
| 3 | 🇧🇷 BR | 16199 |
| 4 | 🇦🇺 AU | 15919 |
| 5 | 🇨🇦 CA | 15378 |
| 6 | 🇮🇹 IT | 14872 |
| 7 | 🇮🇳 IN | 14554 |
| 8 | 🇩🇪 DE | 13182 |
| 9 | 🇨🇴 CO | 12814 |
| 10 | 🇬🇧 GB | 12700 |
| 11 | 🇫🇷 FR | 10911 |
| 12 | 🇯🇵 JP | 10523 |
| 13 | 🇹🇷 TR | 8334 |
| 14 | 🇬🇷 GR | 7912 |
| 15 | 🇲🇽 MX | 7621 |
| 16 | 🇨🇭 CH | 7327 |
| 17 | 🇳🇴 NO | 6801 |
| 18 | 🇹🇭 TH | 4952 |
| 19 | 🇲🇾 MY | 4585 |
| 20 | 🇿🇦 ZA | 4564 |
| 21 | 🇵🇱 PL | 4508 |
| 22 | 🇳🇿 NZ | 3922 |
| 23 | 🇵🇭 PH | 3649 |
| 24 | 🇬🇹 GT | 3462 |
| 25 | 🇭🇷 HR | 3138 |
| 26 | 🇰🇷 KR | 3105 |
| 27 | 🇲🇦 MA | 2723 |
| 28 | 🇲🇪 ME | 2589 |
| 29 | 🇳🇱 NL | 2463 |
| 30 | 🇮🇩 ID | 2281 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5597 |
| 2 | Denver International Airport |  | US | 4505 |
| 3 | Indira Gandhi International Airport |  | IN | 3288 |
| 4 | Tokyo International Airport |  | JP | 3156 |
| 5 | El Dorado International Airport |  | CO | 3065 |
| 6 | Harry Reid International Airport |  | US | 2973 |
| 7 | Zurich Airport |  | CH | 2866 |
| 8 | Guaymaral Airport |  | CO | 2853 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2756 |
| 10 | La Aurora Airport |  | GT | 2634 |
| 11 | Eleftherios Venizelos International Airport |  | GR | 2632 |
| 12 | Salt Lake City International Airport |  | US | 2454 |
| 13 | Congonhas Airport |  | BR | 2355 |
| 14 | Chicago O'Hare International Airport |  | US | 2328 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2259 |
| 16 | Capua Airport |  | IT | 2143 |
| 17 | Madrid Barajas International Airport |  | ES | 2125 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2106 |
| 19 | Frankfurt am Main International Airport |  | DE | 2072 |
| 20 | Enrique Olaya Herrera Airport |  | CO | 1959 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1958 |
| 22 | Charles de Gaulle International Airport |  | FR | 1953 |
| 23 | Malpensa International Airport |  | IT | 1949 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1929 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1840 |
| 26 | Macau International Airport |  | MO | 1796 |
| 27 | Ninoy Aquino International Airport |  | PH | 1795 |
| 28 | Charlotte/Douglas International Airport |  | US | 1722 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1714 |
| 30 | Barcelona International Airport |  | ES | 1701 |
| 31 | Viracopos International Airport |  | BR | 1652 |
| 32 | Kuala Lumpur International Airport |  | MY | 1643 |
| 33 | Seattle-Tacoma International Airport |  | US | 1624 |
| 34 | Norman Y Mineta San Jose International Airport |  | US | 1622 |
| 35 | Calgary International Airport |  | CA | 1568 |
| 36 | Don Mueang International Airport |  | TH | 1561 |
| 37 | Oslo Gardermoen Airport |  | NO | 1547 |
| 38 | Vancouver International Airport |  | CA | 1547 |
| 39 | Bengaluru International Airport |  | IN | 1541 |
| 40 | Reno/Tahoe International Airport |  | US | 1497 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1134 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1042 | 21m | 244 km | 4,387.6 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 767 | 8m | - | - |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 698 | 24m | 225 km | 2,707.9 t |
| 5 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 698 | 1h 6m | 770 km | 9,272.4 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 614 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 460 | 44m | 555 km | 4,404.7 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 444 | 27m | 275 km | 2,103.9 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 436 | 1h 50m | 1,423 km | 10,700.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 423 | 44m | 241 km | 1,757.1 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 395 | 24m | 218 km | 1,488.1 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 382 | 35m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 375 | 23m | 55 km | 356.4 t |
| 14 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 371 | 21m | 250 km | 1,602.5 t |
| 15 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 354 | 12m | - | - |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 353 | 13m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 348 | 1h 6m | 706 km | 4,236.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 344 | 19m | 99 km | 589.2 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 342 | 26m | 215 km | 1,266.6 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 321 | 19m | 144 km | 798.5 t |
| 22 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 320 | 18m | 14 km | 80.0 t |
| 23 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 24 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 312 | 1h 14m | 961 km | 5,171.6 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 310 | 42m | 535 km | 2,863.1 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 298 | 1h 50m | 1,304 km | 6,704.2 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Indira Gandhi International Airport (VIDP) | Pathankot Air Force Station (VIPK) | 274 | 44m | 431 km | 2,039.0 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 274 | 51m | 556 km | 2,626.5 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| OKUUA78 | OKU | Znojmo Airport (LKZN) | Krems Airport (LOAG) | 2026-10-04 08:16 UTC | 2026-10-04 08:30 UTC | 13m |
| FGDTJ | FGD | Rennes-Saint-Jacques Airport (LFRN) | Rennes-Saint-Jacques Airport (LFRN) | 2026-10-04 08:09 UTC | 2026-10-04 08:19 UTC | 9m |
| UAE18V | Emirates | Dubai International Airport (OMDB) | Chhatrapati Shivaji International Airport (VABB) | 2026-10-04 05:56 UTC | 2026-10-04 08:16 UTC | 2h 19m |
| RMF414 | RMF | Sultan Abdul Aziz Shah International Airport (WMSA) | Butterworth Airport (WMKB) | 2026-10-04 07:44 UTC | 2026-10-04 08:13 UTC | 28m |
| HIM678 | HIM | Tribhuvan International Airport (VNKT) | Langtang Airport (VNLT) | 2026-10-04 08:01 UTC | 2026-10-04 08:09 UTC | 8m |
| DFOXI | DFO | Pruszcz Gdański Airport (EPPR) | Pruszcz Gdański Airport (EPPR) | 2026-10-04 07:48 UTC | 2026-10-04 08:07 UTC | 18m |
| NOZ1260 | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Karain Airport (LTXE) | 2026-10-04 04:13 UTC | 2026-10-04 08:04 UTC | 3h 50m |
| FGSAT | FGS | Verona / Boscomantico Airport (LIPN) | Verona / Boscomantico Airport (LIPN) | 2026-10-04 07:04 UTC | 2026-10-04 08:02 UTC | 58m |
| ZKIDU | ZKI | Taieri Airport (NZTI) | Taieri Airport (NZTI) | 2026-10-04 07:37 UTC | 2026-10-04 07:47 UTC | 10m |
| FJJJY | FJJ | Saint-Nazaire-Montoir Airport (LFRZ) | Saint-Nazaire-Montoir Airport (LFRZ) | 2026-10-04 07:28 UTC | 2026-10-04 07:46 UTC | 17m |
| JST031 | JST | Melbourne International Airport (YMML) | Perth International Airport (YPPH) | 2026-10-03 20:58 UTC | 2026-10-04 07:45 UTC | 10h 46m |
| RYR20PT | Ryanair | Shannon Airport (EINN) | Budapest Ferenc Liszt International Airport (LHBP) | 2026-10-04 05:00 UTC | 2026-10-04 07:43 UTC | 2h 43m |
| RYR11DZ | Ryanair | Warsaw Modlin Airport (EPMO) | Otocac Airport (LDRO) | 2026-10-04 06:25 UTC | 2026-10-04 07:42 UTC | 1h 16m |
| AIQ1030 | AIQ | Don Mueang International Airport (VTBD) | Sayaboury Airport (VLSB) | 2026-10-04 06:46 UTC | 2026-10-04 07:35 UTC | 48m |
| DFOXI | DFO | Pruszcz Gdański Airport (EPPR) | Pruszcz Gdański Airport (EPPR) | 2026-10-04 07:15 UTC | 2026-10-04 07:34 UTC | 18m |
| AFR78RT | Air France | Charles de Gaulle International Airport (LFPG) | Lyon Saint-Exupery Airport (LFLL) | 2026-10-04 06:47 UTC | 2026-10-04 07:32 UTC | 45m |
| WMT6UQ | WMT | Memmingen Allgau Airport (EDJA) | Trstenik Airport (LYTR) | 2026-10-04 06:06 UTC | 2026-10-04 07:28 UTC | 1h 21m |
| JA02NA |  | Matsumoto Airport (RJAF) | Matsumoto Airport (RJAF) | 2026-10-04 07:16 UTC | 2026-10-04 07:27 UTC | 11m |
| AFR96TP | Air France | Charles de Gaulle International Airport (LFPG) | Toulouse-Blagnac Airport (LFBO) | 2026-10-04 06:27 UTC | 2026-10-04 07:27 UTC | 1h 0m |
| AFR79TA | Air France | Charles de Gaulle International Airport (LFPG) | Bordeaux-Merignac (BA 106) Airport (LFBD) | 2026-10-04 06:31 UTC | 2026-10-04 07:27 UTC | 55m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
