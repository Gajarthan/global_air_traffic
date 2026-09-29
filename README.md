# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--28_23:59:21_UTC-green)

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

**Latest saved flight:** 2026-09-28 23:59:21 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-09-28 23:59:21 UTC

- **272,048** saved flights
- **79,561** unique routes
- **146** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **272,048** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **3,297,449.8 tonnes** estimated CO2 emissions
- **191,156,509 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 10692 |
| 2 | SkyWest Airlines | 9483 |
| 3 | EJA | 5330 |
| 4 | IndiGo | 4543 |
| 5 | American Airlines | 4225 |
| 6 | Southwest Airlines | 4007 |
| 7 | Delta Air Lines | 3385 |
| 8 | ENY | 3195 |
| 9 | LATAM Airlines | 2624 |
| 10 | AZU | 2555 |
| 11 | Vueling | 2263 |
| 12 | WIF | 2213 |
| 13 | LXJ | 2144 |
| 14 | Lufthansa | 2060 |
| 15 | easyJet | 1816 |
| 16 | Swiss International | 1779 |
| 17 | QLK | 1753 |
| 18 | EJU | 1700 |
| 19 | AXM | 1677 |
| 20 | United Airlines | 1663 |
| 21 | Alaska Airlines | 1605 |
| 22 | All Nippon Airways | 1561 |
| 23 | PGT | 1534 |
| 24 | GLO | 1520 |
| 25 | WMT | 1515 |
| 26 | Air France | 1495 |
| 27 | VIV | 1493 |
| 28 | Wizz Air | 1476 |
| 29 | CXK | 1343 |
| 30 | AEE | 1301 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 226798 |
| 2 | 🇪🇸 ES | 17016 |
| 3 | 🇧🇷 BR | 15955 |
| 4 | 🇦🇺 AU | 15657 |
| 5 | 🇨🇦 CA | 15166 |
| 6 | 🇮🇹 IT | 14687 |
| 7 | 🇮🇳 IN | 14378 |
| 8 | 🇩🇪 DE | 13032 |
| 9 | 🇬🇧 GB | 12574 |
| 10 | 🇨🇴 CO | 12512 |
| 11 | 🇫🇷 FR | 10797 |
| 12 | 🇯🇵 JP | 10412 |
| 13 | 🇹🇷 TR | 8239 |
| 14 | 🇬🇷 GR | 7835 |
| 15 | 🇲🇽 MX | 7518 |
| 16 | 🇨🇭 CH | 7229 |
| 17 | 🇳🇴 NO | 6718 |
| 18 | 🇹🇭 TH | 4865 |
| 19 | 🇲🇾 MY | 4541 |
| 20 | 🇿🇦 ZA | 4528 |
| 21 | 🇵🇱 PL | 4458 |
| 22 | 🇳🇿 NZ | 3830 |
| 23 | 🇵🇭 PH | 3591 |
| 24 | 🇬🇹 GT | 3425 |
| 25 | 🇭🇷 HR | 3098 |
| 26 | 🇰🇷 KR | 3072 |
| 27 | 🇲🇦 MA | 2696 |
| 28 | 🇲🇪 ME | 2548 |
| 29 | 🇳🇱 NL | 2442 |
| 30 | 🇮🇩 ID | 2262 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 5541 |
| 2 | Denver International Airport |  | US | 4438 |
| 3 | Indira Gandhi International Airport |  | IN | 3249 |
| 4 | Tokyo International Airport |  | JP | 3118 |
| 5 | El Dorado International Airport |  | CO | 2978 |
| 6 | Harry Reid International Airport |  | US | 2923 |
| 7 | Guaymaral Airport |  | CO | 2828 |
| 8 | Zurich Airport |  | CH | 2818 |
| 9 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2729 |
| 10 | Eleftherios Venizelos International Airport |  | GR | 2607 |
| 11 | La Aurora Airport |  | GT | 2603 |
| 12 | Salt Lake City International Airport |  | US | 2414 |
| 13 | Congonhas Airport |  | BR | 2323 |
| 14 | Chicago O'Hare International Airport |  | US | 2315 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 2230 |
| 16 | Capua Airport |  | IT | 2100 |
| 17 | Madrid Barajas International Airport |  | ES | 2094 |
| 18 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 2062 |
| 19 | Frankfurt am Main International Airport |  | DE | 2053 |
| 20 | Malpensa International Airport |  | IT | 1934 |
| 21 | Hartsfield/Jackson Atlanta International Airport |  | US | 1932 |
| 22 | Charles de Gaulle International Airport |  | FR | 1931 |
| 23 | Enrique Olaya Herrera Airport |  | CO | 1915 |
| 24 | Sydney Kingsford Smith International Airport |  | AU | 1905 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 1827 |
| 26 | Macau International Airport |  | MO | 1789 |
| 27 | Ninoy Aquino International Airport |  | PH | 1764 |
| 28 | Charlotte/Douglas International Airport |  | US | 1699 |
| 29 | Atizapan De Zaragoza Airport |  | MX | 1694 |
| 30 | Barcelona International Airport |  | ES | 1684 |
| 31 | Viracopos International Airport |  | BR | 1636 |
| 32 | Kuala Lumpur International Airport |  | MY | 1627 |
| 33 | Norman Y Mineta San Jose International Airport |  | US | 1598 |
| 34 | Seattle-Tacoma International Airport |  | US | 1594 |
| 35 | Calgary International Airport |  | CA | 1548 |
| 36 | Don Mueang International Airport |  | TH | 1537 |
| 37 | Bengaluru International Airport |  | IN | 1527 |
| 38 | Oslo Gardermoen Airport |  | NO | 1524 |
| 39 | Vancouver International Airport |  | CA | 1522 |
| 40 | Reno/Tahoe International Airport |  | US | 1457 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1125 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 1021 | 21m | 244 km | 4,299.2 t |
| 3 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 753 | 8m | - | - |
| 4 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 684 | 1h 6m | 770 km | 9,086.4 t |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 679 | 24m | 225 km | 2,634.2 t |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 602 | 12m | - | - |
| 7 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 454 | 44m | 555 km | 4,347.3 t |
| 8 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 438 | 27m | 275 km | 2,075.5 t |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 430 | 1h 50m | 1,423 km | 10,552.9 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 417 | 44m | 241 km | 1,732.1 t |
| 11 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 388 | 24m | 218 km | 1,461.8 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 379 | 35m | - | - |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 367 | 21m | 250 km | 1,585.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 364 | 23m | 55 km | 346.0 t |
| 15 | Bodø Airport (ENBO) | ENEN (ENEN) | 347 | 13m | - | - |
| 16 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 345 | 12m | - | - |
| 17 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 342 | 1h 6m | 706 km | 4,163.9 t |
| 18 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 341 | 19m | 99 km | 584.1 t |
| 19 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 337 | 26m | 215 km | 1,248.1 t |
| 20 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 336 | 1h 39m | 1,156 km | 6,703.1 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 317 | 19m | 144 km | 788.5 t |
| 22 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 23 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 308 | 1h 14m | 961 km | 5,105.3 t |
| 24 | El Dorado International Airport (SKBO) | Madrid Air Base (SKMA) | 302 | 18m | 14 km | 75.5 t |
| 25 | Suvarnabhumi Airport (VTBS) | Surat Thani Airport (VTSB) | 302 | 42m | 535 km | 2,789.2 t |
| 26 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 27 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 295 | 1h 50m | 1,304 km | 6,636.7 t |
| 28 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 286 | 28m | 152 km | 747.4 t |
| 29 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 273 | 15m | 154 km | 723.3 t |
| 30 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 270 | 29m | 304 km | 1,415.4 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N248PA |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-09-28 23:46 UTC | 2026-09-28 23:59 UTC | 12m |
| N815SS |  | Mcgahan Industrial Airpark (AK73) | Kenai Municipal Airport (PAEN) | 2026-09-28 23:47 UTC | 2026-09-28 23:59 UTC | 11m |
| VLL | VLL | Mackay Airport (YBMK) | Moranbah Airport (YMRB) | 2026-09-28 23:23 UTC | 2026-09-28 23:57 UTC | 34m |
| YGQ | YGQ | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-09-28 23:24 UTC | 2026-09-28 23:53 UTC | 29m |
| ERU30 | ERU | Robin Airport (59AZ) | Cottonwood Airport (KP52) | 2026-09-28 23:38 UTC | 2026-09-28 23:52 UTC | 13m |
| TKR181 | TKR | Robert Gray Army Air Field (KGRK) | Kimble County Airport (KJCT) | 2026-09-28 23:28 UTC | 2026-09-28 23:51 UTC | 23m |
| CXK366 | CXK | Hayward Executive Airport (KHWD) | Hayward Executive Airport (KHWD) | 2026-09-28 23:10 UTC | 2026-09-28 23:47 UTC | 37m |
| TFX | TFX | Halls Creek Airport (YHLC) | Halls Creek Airport (YHLC) | 2026-09-28 23:36 UTC | 2026-09-28 23:47 UTC | 10m |
| N669FG |  | Trenton Mercer Airport (KTTN) | Lehigh Valley International Airport (KABE) | 2026-09-28 23:00 UTC | 2026-09-28 23:45 UTC | 45m |
| N6913S |  | Steamboat Springs/Bob Adams Field (KSBS) | Eagle Soaring Airport (1CD4) | 2026-09-28 23:33 UTC | 2026-09-28 23:44 UTC | 10m |
| N27AU |  | Andrews University Airpark (KC20) | Andrews University Airpark (KC20) | 2026-09-28 22:05 UTC | 2026-09-28 23:41 UTC | 1h 36m |
| N401SE |  | Tampa International Airport (KTPA) | Capital City Airport (KCXY) | 2026-09-28 20:14 UTC | 2026-09-28 23:40 UTC | 3h 25m |
| FFL237 | FFL | Charles M Schulz/Sonoma County Airport (KSTS) | Agape Farm Airport (OR42) | 2026-09-28 22:31 UTC | 2026-09-28 23:39 UTC | 1h 7m |
| EJA386 | EJA | Lincoln Airport (KLNK) | Lincoln Airport (KLNK) | 2026-09-28 22:58 UTC | 2026-09-28 23:34 UTC | 35m |
| N5292D |  | San Gabriel Valley Airport (KEMT) | Big Bear City Airport (KL35) | 2026-09-28 22:51 UTC | 2026-09-28 23:30 UTC | 39m |
| N469MB |  | Daytona Beach International Airport (KDAB) | The 2A Ranch Airport (0FD0) | 2026-09-28 22:58 UTC | 2026-09-28 23:30 UTC | 31m |
| YMV | YMV | Aeropelican Airport (YPEC) | Aeropelican Airport (YPEC) | 2026-09-28 23:08 UTC | 2026-09-28 23:27 UTC | 19m |
| STMPD19 | STM | Camp Pendleton Mcas (Munn Field) Airport (KNFG) | Miramar Mcas (Joe Foss Field) Airport (KNKX) | 2026-09-28 23:13 UTC | 2026-09-28 23:27 UTC | 13m |
| N530JL |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-09-28 22:02 UTC | 2026-09-28 23:26 UTC | 1h 23m |
| QLK20D | QLK | Sydney Kingsford Smith International Airport (YSSY) | Walcha Airport (YWCH) | 2026-09-28 22:48 UTC | 2026-09-28 23:23 UTC | 35m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
