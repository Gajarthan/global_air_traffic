# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--15_11:17:58_UTC-green)

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

**Latest saved flight:** 2026-06-15 11:17:58 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-15 11:17:58 UTC

- **111,138** saved flights
- **38,748** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **111,138** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,359,452.4 tonnes** estimated CO2 emissions
- **78,808,837 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4593 |
| 2 | SkyWest Airlines | 4152 |
| 3 | IndiGo | 2180 |
| 4 | EJA | 2150 |
| 5 | American Airlines | 1749 |
| 6 | Southwest Airlines | 1662 |
| 7 | ENY | 1381 |
| 8 | Delta Air Lines | 1312 |
| 9 | Lufthansa | 1257 |
| 10 | Vueling | 1021 |
| 11 | WIF | 982 |
| 12 | LATAM Airlines | 981 |
| 13 | AXM | 936 |
| 14 | AZU | 921 |
| 15 | LXJ | 851 |
| 16 | Swiss International | 799 |
| 17 | All Nippon Airways | 774 |
| 18 | Alaska Airlines | 755 |
| 19 | QLK | 730 |
| 20 | easyJet | 715 |
| 21 | EJU | 707 |
| 22 | Cathay Pacific | 659 |
| 23 | AEE | 628 |
| 24 | VIV | 623 |
| 25 | Air France | 622 |
| 26 | United Airlines | 617 |
| 27 | MXY | 593 |
| 28 | CXK | 581 |
| 29 | AXB | 547 |
| 30 | GLO | 545 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 93439 |
| 2 | 🇪🇸 ES | 7635 |
| 3 | 🇮🇳 IN | 6871 |
| 4 | 🇦🇺 AU | 6606 |
| 5 | 🇧🇷 BR | 6141 |
| 6 | 🇮🇹 IT | 5993 |
| 7 | 🇩🇪 DE | 5952 |
| 8 | 🇨🇦 CA | 5836 |
| 9 | 🇯🇵 JP | 5035 |
| 10 | 🇬🇧 GB | 4773 |
| 11 | 🇫🇷 FR | 4445 |
| 12 | 🇨🇴 CO | 3775 |
| 13 | 🇲🇽 MX | 3297 |
| 14 | 🇬🇷 GR | 3164 |
| 15 | 🇳🇴 NO | 3077 |
| 16 | 🇨🇭 CH | 2848 |
| 17 | 🇲🇾 MY | 2418 |
| 18 | 🇹🇷 TR | 2210 |
| 19 | 🇿🇦 ZA | 1893 |
| 20 | 🇰🇷 KR | 1845 |
| 21 | 🇹🇭 TH | 1836 |
| 22 | 🇵🇱 PL | 1822 |
| 23 | 🇳🇿 NZ | 1822 |
| 24 | 🇵🇭 PH | 1621 |
| 25 | 🇬🇹 GT | 1588 |
| 26 | 🇲🇦 MA | 1225 |
| 27 | 🇲🇴 MO | 1151 |
| 28 | 🇲🇪 ME | 1090 |
| 29 | 🇳🇱 NL | 1084 |
| 30 | 🇭🇷 HR | 968 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2366 |
| 2 | Denver International Airport |  | US | 1884 |
| 3 | Tokyo International Airport |  | JP | 1669 |
| 4 | Indira Gandhi International Airport |  | IN | 1493 |
| 5 | Guaymaral Airport |  | CO | 1405 |
| 6 | Harry Reid International Airport |  | US | 1400 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1381 |
| 8 | Zurich Airport |  | CH | 1250 |
| 9 | Frankfurt am Main International Airport |  | DE | 1230 |
| 10 | La Aurora Airport |  | GT | 1221 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1193 |
| 12 | Macau International Airport |  | MO | 1151 |
| 13 | El Dorado International Airport |  | CO | 1135 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1113 |
| 15 | Chicago O'Hare International Airport |  | US | 1102 |
| 16 | Madrid Barajas International Airport |  | ES | 970 |
| 17 | Capua Airport |  | IT | 966 |
| 18 | Salt Lake City International Airport |  | US | 941 |
| 19 | Kuala Lumpur International Airport |  | MY | 941 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 934 |
| 21 | Congonhas Airport |  | BR | 856 |
| 22 | Charlotte/Douglas International Airport |  | US | 854 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 836 |
| 24 | Charles de Gaulle International Airport |  | FR | 834 |
| 25 | Bengaluru International Airport |  | IN | 829 |
| 26 | Malpensa International Airport |  | IT | 811 |
| 27 | General Edward Lawrence Logan International Airport |  | US | 756 |
| 28 | Ninoy Aquino International Airport |  | PH | 748 |
| 29 | Daniel K Inouye International Airport |  | US | 737 |
| 30 | Tenerife Norte Airport |  | ES | 733 |
| 31 | Barcelona International Airport |  | ES | 727 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 727 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 711 |
| 34 | Don Mueang International Airport |  | TH | 669 |
| 35 | Amsterdam Airport Schiphol |  | NL | 667 |
| 36 | Vitoria/Foronda Airport |  | ES | 660 |
| 37 | Calgary International Airport |  | CA | 656 |
| 38 | Seattle-Tacoma International Airport |  | US | 639 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 638 |
| 40 | Viracopos International Airport |  | BR | 629 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 583 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 405 | 21m | 244 km | 1,705.3 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 295 | 24m | 225 km | 1,144.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 286 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 284 | 1h 7m | 706 km | 3,457.7 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 272 | 1h 25m | 910 km | 4,268.3 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 262 | 1h 10m | 770 km | 3,480.5 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 225 | 19m | 165 km | 640.0 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 222 | 26m | 275 km | 1,052.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 209 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 166 | 20m | 99 km | 284.3 t |
| 14 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 162 | 27m | 215 km | 600.0 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 161 | 22m | 55 km | 153.0 t |
| 16 | Bodø Airport (ENBO) | ENEN (ENEN) | 158 | 13m | - | - |
| 17 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 153 | 27m | 152 km | 399.8 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 151 | 31m | 369 km | 961.2 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 147 | 44m | 452 km | 1,145.7 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 146 | 18m | 144 km | 363.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 142 | 20m | 250 km | 613.4 t |
| 23 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 141 | 44m | 241 km | 585.7 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 134 | 1h 1m | 695 km | 1,606.3 t |
| 25 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 132 | 1h 43m | 1,423 km | 3,239.5 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 132 | 1h 39m | 1,156 km | 2,633.4 t |
| 28 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 124 | 24m | 223 km | 477.0 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 124 | 1h 17m | 961 km | 2,055.4 t |
| 30 | Calgary International Airport (CYYC) | Moose Jaw Municipal Airport (CJS4) | 124 | 1h 2m | 611 km | 1,307.8 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| XGN | XGN | Tamworth Airport (YSTW) | Tamworth Airport (YSTW) | 2026-06-15 10:30 UTC | 2026-06-15 11:17 UTC | 47m |
| CXK1133 | CXK | St Pete-Clearwater International Airport (KPIE) | St Pete-Clearwater International Airport (KPIE) | 2026-06-15 11:02 UTC | 2026-06-15 11:17 UTC | 15m |
| CAP329 | CAP | KWSD (KWSD) | KWSD (KWSD) | 2026-06-15 10:34 UTC | 2026-06-15 10:46 UTC | 12m |
| GKLUB | GKL | Turweston Airport (EGBT) | Wellesbourne Mountford Airport (EGBW) | 2026-06-15 10:34 UTC | 2026-06-15 10:41 UTC | 7m |
| EWG3PV | EWG | Palma De Mallorca Airport (LEPA) | Leverkusen Airport (EDKL) | 2026-06-15 08:22 UTC | 2026-06-15 10:29 UTC | 2h 7m |
| SWR2PH | Swiss International | Graz Airport (LOWG) | Zurich Airport (LSZH) | 2026-06-15 09:27 UTC | 2026-06-15 10:29 UTC | 1h 1m |
| IBB97FU | IBB | Tenerife Norte Airport (GCXO) | La Morgal Airport (LEMR) | 2026-06-15 07:58 UTC | 2026-06-15 10:26 UTC | 2h 28m |
| N7925M |  | El Paso International Airport (KELP) | KWSD (KWSD) | 2026-06-15 09:50 UTC | 2026-06-15 10:24 UTC | 33m |
| EZS1571 | EZS | Geneva Cointrin International Airport (LSGG) | Birmingham International Airport (EGBB) | 2026-06-15 08:42 UTC | 2026-06-15 10:24 UTC | 1h 41m |
| RY100T |  | East Midlands Airport (EGNX) | East Midlands Airport (EGNX) | 2026-06-15 09:35 UTC | 2026-06-15 10:23 UTC | 48m |
| JAL613M | Japan Airlines | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 2026-06-15 09:03 UTC | 2026-06-15 10:23 UTC | 1h 20m |
| TVF25FR | TVF | Paris-Orly Airport (LFPO) | Ifrane Airport (GMFI) | 2026-06-15 08:07 UTC | 2026-06-15 10:23 UTC | 2h 15m |
| CFG5PC | CFG | Palma De Mallorca Airport (LEPA) | Wipperfurth-Neye Airport (EDKN) | 2026-06-15 08:00 UTC | 2026-06-15 10:22 UTC | 2h 21m |
| DHUGO | DHU | Ecuvillens Airport (LSGE) | Raron Airport (LSTA) | 2026-06-15 09:18 UTC | 2026-06-15 10:21 UTC | 1h 2m |
| UFX64 | UFX | Blackpool International Airport (EGNH) | Blackpool International Airport (EGNH) | 2026-06-15 09:49 UTC | 2026-06-15 10:20 UTC | 31m |
| NHZ31 | NHZ | Blackpool International Airport (EGNH) | RAF Woodvale (EGOW) | 2026-06-15 10:04 UTC | 2026-06-15 10:17 UTC | 12m |
| DLH1KK | Lufthansa | Munich International Airport (EDDM) | Capua Airport (LIAU) | 2026-06-15 09:12 UTC | 2026-06-15 10:14 UTC | 1h 1m |
| IGO273 | IndiGo | Juhu Aerodrome (VAJJ) | VARK (VARK) | 2026-06-15 09:37 UTC | 2026-06-15 10:12 UTC | 35m |
| NOZ1190 | Norwegian Air | Oslo Gardermoen Airport (ENGM) | Helsinki Vantaa Airport (EFHK) | 2026-06-15 09:04 UTC | 2026-06-15 10:11 UTC | 1h 7m |
| HBIAW | HBI | Lugano Airport (LSZA) | Sondrio Caiolo Airport (LILO) | 2026-06-15 09:54 UTC | 2026-06-15 10:09 UTC | 15m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
