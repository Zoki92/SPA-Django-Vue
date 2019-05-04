import moment from 'moment'

export const timeFormatter = {
    filters: {
        timeAgo: function (value) {
            return moment.utc(value).fromNow()
        }
    }
}